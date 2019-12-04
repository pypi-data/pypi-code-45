import sys
from .pull_check import pull_check

from .load_env_files import load_env_files
from .load_bundle import load_bundle

def api_pull(config):

  load_env_files(config)
  load_bundle(config)

  pull_check_result = pull_check(config['files_compose'], env=config['environ'], verbose=True)
  if(pull_check_result['error']):
    sys.exit(1)