import pytest
import unittest
from unittest.mock import patch

from copy import deepcopy, copy
from pathlib import Path
import json

from startwork.models.CreateProject import CreateProject
from startwork.models.DeleteProject import DeleteProject

prompt_mock_values = [
  {"name": "sample_name1", "project_path": "/home"},
  {"name": "sample_name2", "project_path": "/home"},
  {"name": "sample_name3", "project_path": "/home"},
]

class TestDeleteProject(unittest.TestCase):
  # CLASS SETUP
  project_list_path = Path(__file__).parent / "projects_list.json"
  prompt_mock_values = deepcopy(prompt_mock_values)

  @pytest.fixture(autouse=True)
  def _capsys(self, capsys):
    self.capsys = capsys

  # TESTS
  def test_if_is_function(self):
    assert callable(DeleteProject.run)

  @patch(
    "startwork.models.CreateProject.prompt",
    return_value=prompt_mock_values[0]
  )
  @patch(
    "startwork.models.DeleteProject.prompt",
    return_value=prompt_mock_values[0]
  )
  def test_happy_path(self, mock_inquirer_prompt):
    # set json for the test
    for prompt_value in prompt_mock_values:
      mock_inquirer_prompt.return_value["name"] = copy(prompt_value["name"])
      mock_inquirer_prompt.return_value["project_path"] = copy(prompt_value["project_path"])

      CreateProject.run(self.project_list_path)

    with open(self.project_list_path, "r") as file:
      assert json.load(file) == prompt_mock_values

    # do the test it self
    for prompt_value in prompt_mock_values:
      mock_inquirer_prompt.return_value["name"] = copy(prompt_value["name"])
      mock_inquirer_prompt.return_value["project_path"] = copy(prompt_value["project_path"])

      DeleteProject.run(self.project_list_path)

      out, err = self.capsys.readouterr()
      assert out == f'Project named as "{prompt_mock_values["name"]}" has been deleted!'
      assert err == ""
      # asset comparing array removing each item at time

    with open(self.project_list_path, "r") as file:
      assert json.load(file) == []
