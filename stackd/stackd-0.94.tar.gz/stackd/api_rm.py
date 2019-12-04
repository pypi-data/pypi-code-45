import sys
from .cmd_rm import cmd_rm

from .load_env_files import load_env_files

def api_rm(config, args=[]):

  load_env_files(config)

  process = cmd_rm(config, args)

  if(process.returncode != 0):
      sys.exit(process.returncode)