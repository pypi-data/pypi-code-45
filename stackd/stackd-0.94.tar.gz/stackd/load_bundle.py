from .load_vars_files import load_vars_files
from .load_vars_data import load_vars_data
from .load_compose import load_compose

def load_bundle(config):
  load_vars_files(config['files_vars'], config['env_vars'])
  load_vars_data(config['files_vars'], config['vars_data'])
  load_compose(config)
