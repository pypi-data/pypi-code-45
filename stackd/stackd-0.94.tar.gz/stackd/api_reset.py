from .cmd_clear import cmd_clear
from .cmd_deploy import cmd_deploy

from .load_env_files import load_env_files
from .load_bundle import load_bundle
from .load_hash_versions import load_hash_versions

def api_reset(config):
  load_env_files(config)
  load_bundle(config)
  load_hash_versions(config)

  cmd_clear(config)
  cmd_deploy(config, args)