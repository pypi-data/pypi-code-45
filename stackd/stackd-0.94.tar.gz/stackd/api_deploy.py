import sys
from .cmd_deploy import cmd_deploy

from .load_env_files import load_env_files
from .load_bundle import load_bundle
from .load_hash_versions import load_hash_versions

def api_deploy(config, args=[]):

  load_env_files(config)
  load_bundle(config)
  load_hash_versions(config)

  process = cmd_deploy(config, args)
  if(process.returncode != 0):
    sys.exit(process.returncode)
