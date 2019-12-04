import sys

from .cmd_clear import cmd_clear
from .printError import printError

from .load_env_files import load_env_files

def api_clear(config):
  load_env_files(config)
  process = cmd_clear(config)
  if(process and process.returncode != 0):
      printError('ERROR: command failed with exit code '+str(process.returncode))
      sys.exit(process.returncode)