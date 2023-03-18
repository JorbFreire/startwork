import json
from os import getcwd
from inquirer import errors, Text, Path, prompt

def _raiseError(reason):
  raise errors.ValidationError('', reason=reason)

def _validate_name(current, projects_list):
  if len(current) < 1:
    _raiseError("Project name can't be empty")

  for project in projects_list:
    if project["name"] == current:
      _raiseError(f'Name "{current}" alredy in use')

  return True

def create_project(project_list_path):
  projects_list = []

  with open(project_list_path, 'r') as openfile:
    projects_list = json.load(openfile)

  questions = [
    Text(
      'name',
      message="What's the project name?",
      validate=lambda answers, current: _validate_name(
        current,
        projects_list
      )
    ),
    Path(
      'project_path',
      message="Where is the project located?",
      path_type=Path.DIRECTORY,
      exists=True,
      normalize_to_absolute_path=True,
      default=getcwd()
    ),
  ]

  new_project = prompt(questions)
  if new_project:
    projects_list.append(new_project)

  with open(project_list_path, "w") as outfile:
    outfile.write(json.dumps(projects_list, indent=4))

  if new_project:
    print("New project created!")
