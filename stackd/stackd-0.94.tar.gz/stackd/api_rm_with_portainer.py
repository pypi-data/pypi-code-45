import sys
from .run_portainer_stack_up import run_portainer_stack_up

from .load_env_files import load_env_files
from .load_bundle import load_bundle
from .load_hash_versions import load_hash_versions

def api_rm_with_portainer(config, args=[]):

  load_env_files(config)
  load_bundle(config)
  load_hash_versions(config)

  process = run_portainer_stack_up(config, ['-a','undeploy', args])
  if(process.returncode != 0):
      sys.exit(process.returncode)