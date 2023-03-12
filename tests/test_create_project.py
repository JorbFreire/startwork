import pytest
from pathlib import Path
from startwork.actions.create_project import create_project


class TestCreateProject:
  project_list_path = Path(__file__).parent / "projects_list.json"
  
  def test_if_is_function(self):
    assert callable(create_project)

  @pytest.fixture(params=['nodict', 'dict'])
  def test_happy_path(self):
    create_project(self.project_list_path)
    assert True
