import os
import copy

from .load_env_defaults import load_env_defaults
from .load_env_files import load_env_files
from .load_vars_files import load_vars_files
from .load_vars_data import load_vars_data
from .load_compose import load_compose
from .load_hash_versions import load_hash_versions

from .cmd_deploy import cmd_deploy

def cmd_stacks_up(config, stacks, args=[]):

  load_vars_files(config['files_vars'], config['env_vars'])
  load_vars_data(config['files_vars'], config['vars_data'])

  cwd = os.getcwd()
  for stack in stacks:
    stack_path = stack['path']
    os.chdir(stack_path)
    environ = config['environ'].copy()

    sub_config = {
      'env_vars': copy.copy(config['env_vars']),
      'vars_data': copy.deepcopy(config['env_vars']),
      'environ': environ,
      'files_env': [],
      'files_compose_src': [],
      'files_compose': [],
      'files_build_compose_src': [],
      'files_build_compose': [],
      'files_vars': [],
    }
    del sub_config['environ']['STACKD_STACK_NAME']
    load_env_defaults(sub_config['env_vars'], sub_config['environ'])
    load_env_files(sub_config)

    load_vars_files(sub_config['files_vars'], sub_config['env_vars'])
    load_vars_data(sub_config['files_vars'], sub_config['vars_data'])
    load_compose(sub_config)

    load_hash_versions(sub_config)

    cmd_deploy(sub_config, args)

    os.chdir(cwd)
