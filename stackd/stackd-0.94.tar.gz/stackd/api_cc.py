import sys
from .cmd_cc import cmd_cc

from .load_env_files import load_env_files


def api_cc(config):
  load_env_files(config)

  process = cmd_cc(config['env_vars'])
  
  if(process.returncode != 0):
      sys.exit(process.returncode)