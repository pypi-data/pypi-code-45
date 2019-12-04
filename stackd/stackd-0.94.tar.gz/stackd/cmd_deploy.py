import sys
from distutils.util import strtobool
from .pull_check import pull_check
from .run_shell import run_shell
from .autocreate_networks import autocreate_networks
from .build_stack_compose_file import build_stack_compose_file
from .build_stack_env_file import build_stack_env_file
from .paths import get_bundle_stack_compose_file_path

def cmd_deploy(config, args=[]):

  files_compose = config['files_compose']
  env_vars = config['env_vars']

  build_stack_compose_file(config)
  build_stack_env_file(config['env_vars'])
  compose_file = get_bundle_stack_compose_file_path(config['env_vars'])

  enabled_pull_check = strtobool(env_vars['STACKD_DEPLOY_PULL_CHECK'])
  if(enabled_pull_check):
    pull_check_result = pull_check([compose_file], env=config['environ'], verbose=True)
    if(pull_check_result['error']):
      print("\nError: unable to pull missing required images")
      sys.exit(1)

  p = autocreate_networks(config)
  if p != True:
    return p

  parameters = env_vars['STACKD_DEPLOY_PARAMETERS']
  prune = strtobool(env_vars['STACKD_DEPLOY_PRUNE'])
  if(prune):
    parameters += " --prune"
  regauth = strtobool(env_vars['STACKD_DEPLOY_WITH_REGISTRY_AUTH'])
  if(regauth):
    parameters += " --with-registry-auth"

  process = run_shell([
    'docker','stack','deploy',
    parameters,
    '-c',compose_file,
    env_vars['STACKD_STACK_NAME'],
    args,
  ], env=config['environ'])

  return process
