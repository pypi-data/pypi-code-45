import sys
from .cmd_vc import cmd_vc

from .load_env_files import load_env_files

def api_vc(config):

  load_env_files(config)

  process = cmd_vc(config['env_vars'])
  if(process.returncode != 0):
      sys.exit(process.returncode)