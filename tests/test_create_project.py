import pytest
from pathlib import Path
from startwork.actions.create_project import create_project
import unittest
import json

from unittest.mock import patch

prompt_mock_value = [
  {"name": "sample_name", "project_path": "/home"},
  {"name": "sample_name2", "project_path": "/home"},
  {"name": "sample_name3", "project_path": "/home"},
]

class TestCreateProject(unittest.TestCase):
  # CLASS SETUP
  project_list_path = Path(__file__).parent / "projects_list.json"

  @pytest.fixture(autouse=True)
  def _capsys(self, capsys):
    self.capsys = capsys

  # TESTS
  def test_if_is_function(self):
    assert callable(create_project)

  @patch(
    "startwork.actions.create_project.prompt",
    return_value=prompt_mock_value[0]
  )
  def test_happy_path(self, mock_inquirer_prompt):
    create_project(self.project_list_path)
    out, err = self.capsys.readouterr()
    assert out == "New project created!\n"
    assert err == ''

    test_list = []
    with open(self.project_list_path, "r") as file:
      test_list = json.load(file)

    assert test_list == prompt_mock_value[0]

  # @patch(
  #   "startwork.actions.create_project.prompt",
  #   return_value=prompt_mock_value[0]
  # )
  # def test_repeated_name(self, mock_inquirer_prompt):
  #   create_project(self.project_list_path)
  #   out, err = self.capsys.readouterr()
  #   assert out == ""
  #   assert err == f'Name "{mock_inquirer_prompt.name}" alredy in use'
