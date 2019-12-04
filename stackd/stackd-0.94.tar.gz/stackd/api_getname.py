from .load_env_files import load_env_files
def api_getname(config):
  load_env_files(config)
  print(config['env_vars']['STACKD_STACK_NAME'])