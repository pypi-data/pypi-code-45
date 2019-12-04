import sys
from os import path

import yaml

from .run_shell import run_shell
from .printError import printError

from .load_env_files import load_env_files

from .cmd_stacks_up import cmd_stacks_up
from .cmd_stacks_rm import cmd_stacks_rm
from .cmd_stacks_logs import cmd_stacks_logs

def api_stacks(config, args=[]):

  load_env_files(config)

  if len(args) == 0:
    printError('ERROR: missing command argument for stackd stacks: up|rm|logs')
    sys.exit(1)

  env_vars = config['env_vars']

  cmd = args.pop(0)

  stacks = get_stacks()

  if cmd == "up" or cmd == "deploy":
    cmd_stacks_up(config, stacks, args)
  elif cmd == "rm":
    cmd_stacks_rm(config, stacks, args)
  elif cmd == "logs":
    cmd_stacks_logs(config, stacks, args)
  else:
    printError('ERROR: unknown command "'+cmd+'" for stackd stacks')
    sys.exit(1)


def get_stacks():
  config_file = 'stacks.yml'
  if not path.exists(config_file):
    printError('ERROR: stacks.yml not found in current directory')
    sys.exit(1)

  with open(config_file, 'r') as content_file:
    yaml_dump = content_file.read().strip()
    stacks_config = yaml.safe_load(yaml_dump)

  if 'stacks_dir' in stacks_config:
    stacks_dir = stacks_config["stacks_dir"]
  else:
    stacks_dir = "."
  stacks = []

  for stack_config in stacks_config["stacks"]:
    if type(stack_config) == str:
      stack_config = {"name":stack_config}
    if path not in stack_config:
      stack_config['path'] = stacks_dir+"/"+stack_config['name']
    stacks.append(stack_config)

  return stacks
