import sys
from .pull_check import pull_check
from .cmd_update import cmd_update

from .load_env_files import load_env_files
from .load_bundle import load_bundle
from .load_hash_versions import load_hash_versions

def api_upgrade(config, args=[]):

  load_env_files(config)
  load_bundle(config)
  load_hash_versions(config)

  pull_check_result = pull_check(config['files_compose'], env=config['environ'], verbose=True)
  if(pull_check_result['error']):
    sys.exit(1)

  process = cmd_update(config, args)
  if(process and process.returncode != 0):
    sys.exit(process.returncode)
