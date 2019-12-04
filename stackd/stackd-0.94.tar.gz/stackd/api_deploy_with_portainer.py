import sys
from distutils.util import strtobool
from .pull_check import pull_check
from .run_portainer_stack_up import run_portainer_stack_up

from .load_env_files import load_env_files
from .load_bundle import load_bundle
from .load_hash_versions import load_hash_versions

def api_deploy_with_portainer(config, args=[]):

  load_env_files(config)
  load_bundle(config)
  load_hash_versions(config)

  enabled_pull_check = strtobool(config['env_vars']['STACKD_DEPLOY_PULL_CHECK'])
  if(enabled_pull_check):
    pull_check_result = pull_check(config['files_compose'], env=config['environ'], verbose=True)
    if(pull_check_result['error']):
      print("\nError: unable to pull missing required images")
      sys.exit(1)

  process = run_portainer_stack_up(config, ['-a','deploy', args])
  if(process.returncode != 0):
      sys.exit(process.returncode)