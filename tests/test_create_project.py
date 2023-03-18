import pytest
import unittest
from unittest.mock import patch

from copy import deepcopy, copy
from pathlib import Path
import json
from inquirer.errors import ValidationError as InquirerValidationError

from startwork.actions.create_project import create_project, _validate_name

prompt_mock_values = [
  {"name": "sample_name1", "project_path": "/home"},
  {"name": "sample_name2", "project_path": "/home"},
  {"name": "sample_name3", "project_path": "/home"},
]

class TestCreateProject(unittest.TestCase):
  # CLASS SETUP
  project_list_path = Path(__file__).parent / "projects_list.json"
  prompt_mock_values = deepcopy(prompt_mock_values)
  
  def _get_error(self, error, current=""):
    if error == "empty":
      return InquirerValidationError("", reason="Project name can't be empty")
    if error == "alredy_used" and len(current) > 1:
      return InquirerValidationError("", reason=f'Name "{current}" alredy in use') 

  @pytest.fixture(autouse=True)
  def _capsys(self, capsys):
    self.capsys = capsys

  # TESTS
  def test_if_is_function(self):
    assert callable(create_project)

  @patch(
    "startwork.actions.create_project.prompt",
    return_value=prompt_mock_values[0]
  )
  def test_happy_path(self, mock_inquirer_prompt):
    for prompt_value in prompt_mock_values:
      mock_inquirer_prompt.return_value["name"] = copy(prompt_value["name"])
      mock_inquirer_prompt.return_value["project_path"] = copy(prompt_value["project_path"])

      create_project(self.project_list_path)
      out, err = self.capsys.readouterr()
      assert out == "New project created!\n"
      assert err == ""

    with open(self.project_list_path, "r") as file:
      assert json.load(file) == prompt_mock_values

    # clean json for the next test 
    with open(self.project_list_path, "w") as outfile:
      outfile.write(json.dumps([], indent=4))

    with open(self.project_list_path, "r") as file:
      assert json.load(file) == []

  def test_validate_name_happy_path(self):
    try:
      is_valid_name = _validate_name("aa", prompt_mock_values)
      out, err = self.capsys.readouterr()

      assert out == ""
      assert err == ""
      assert is_valid_name
    except Exception:
      assert False  

  def test_validate_name_string_length(self):
    try:
      _validate_name("", prompt_mock_values)
      assert False
    except Exception as exception:
      expected_exception = self._get_error("empty")
      assert exception.__module__ == expected_exception.__module__
      assert exception.reason == expected_exception.reason
      assert exception.value == expected_exception.value

  def test_validate_name_alredy_used(self):
    for prompt_value in prompt_mock_values:
      try:
        _validate_name(prompt_value["name"], prompt_mock_values)
        assert False
      except Exception as exception:
        expected_exception = self._get_error("alredy_used", prompt_value["name"])
        assert exception.__module__ == expected_exception.__module__
        assert exception.reason == expected_exception.reason
        assert exception.value == expected_exception.value
