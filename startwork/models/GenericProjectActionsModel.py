from inquirer import errors

class GenericProjectActionsModel:
  @staticmethod
  def _raiseError(reason):
    raise errors.ValidationError('', reason=reason)

  @staticmethod
  def _validate_name(current, projects_list):
    if len(current) < 1:
      GenericProjectActionsModel._raiseError("Project name can't be empty")

    for project in projects_list:
      if project["name"] == current:
        GenericProjectActionsModel._raiseError(f'Name "{current}" alredy in use')

    return True
