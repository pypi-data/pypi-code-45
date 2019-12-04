import sys

# import pprint
import yaml

from .style import style

from .load_env_files import load_env_files
from .load_bundle import load_bundle
from .load_hash_versions import load_hash_versions

def api_infos(config):
  load_env_files(config)
  load_bundle(config)
  load_hash_versions(config)

  print('STACKD ENVIRONMENT 🦊:')
  print('\n'+style.UNDERLINE('stack name:') + ' ' + config['env_vars']['STACKD_STACK_NAME'])

  print('\n'+style.UNDERLINE('.env files:'))
  for file in config['files_env']:
    print(file)

  print('\n'+style.UNDERLINE('vars files:'))
  for file in config['files_vars']:
    print(file)

  print('\n'+style.UNDERLINE('stack compose files:'))
  i = 0
  for file in config['files_compose_src']:
    print(file+' ('+config['files_compose'][i]+')')
    i = i+1

  print('\n'+style.UNDERLINE('build compose files:'))
  i = 0
  for file in config['files_build_compose_src']:
    print(file+' ('+config['files_build_compose'][i]+')')
    i = i+1

  print('\n'+style.UNDERLINE('jinja variables:'))
  # pp = pprint.PrettyPrinter(indent=2)
  # pp.pprint(vars_data)
  yaml.safe_dump(config['vars_data'], sys.stdout, default_flow_style=False, indent=2)

  print('\n'+style.UNDERLINE('env variables:'))
  for key, val in config['env_vars'].items() :
    print(key + '=' + val)
