from .build_stack_compose_file import build_stack_compose_file
from .build_stack_env_file import build_stack_env_file

from .load_env_files import load_env_files
from .load_bundle import load_bundle
from .load_hash_versions import load_hash_versions

def api_bundle(config):

  load_env_files(config)
  load_bundle(config)
  load_hash_versions(config)

  build_stack_compose_file(config)
  build_stack_env_file(config['env_vars'])
  print('bundle created in "'+config['env_vars']['STACKD_BUNDLE_DIR']+'"')