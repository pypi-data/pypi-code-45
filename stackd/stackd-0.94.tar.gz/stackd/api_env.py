from .load_env_files import load_env_files
def api_env(config):
  load_env_files(config)
  env_vars = config['env_vars']
  for env_key in env_vars:
    print(env_key + '=' + env_vars[env_key])