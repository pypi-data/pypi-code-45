from .cmd_exec import cmd_exec

from .load_env_files import load_env_files

def api_exec(config, args):

  load_env_files(config)

  cmd_exec(config['env_vars'], args)
