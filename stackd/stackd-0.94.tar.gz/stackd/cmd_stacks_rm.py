import os

from .load_env_defaults import load_env_defaults
from .load_env_files import load_env_files
from .cmd_rm import cmd_rm

def cmd_stacks_rm(config, stacks, args=[]):

  cwd = os.getcwd()
  for stack in stacks:
    stack_path = stack['path']
    os.chdir(stack_path)
    environ = config['environ'].copy()

    sub_config = {
      'env_vars': {},
      'vars_data': {},
      'files_env': [],
      'files_compose_src': [],
      'files_compose': [],
      'files_build_compose_src': [],
      'files_build_compose': [],
      'files_vars': [],
      'environ': environ,
    }
    load_env_defaults(sub_config['env_vars'], sub_config['environ'])

    load_env_files(sub_config)
    cmd_rm(sub_config, args)

    os.chdir(cwd)
