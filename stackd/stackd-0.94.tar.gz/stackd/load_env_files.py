from .load_env_file import load_env_file

def load_env_files(config):
  load_env_file('.env.default', config)
  load_env_file('.env', config)
  env_ls = config['env_vars']['STACKD_ENV'].split(',')
  for env_key in env_ls:
    load_env_file('.env.' + env_key, config)
  return config['files_env']