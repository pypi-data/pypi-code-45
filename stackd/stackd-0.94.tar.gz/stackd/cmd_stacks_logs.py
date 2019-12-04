import os
import copy
import subprocess

from .load_env_defaults import load_env_defaults
from .load_env_files import load_env_files

from .services_logs import services_logs

def cmd_stacks_logs(config, stacks, args=[]):
  env_vars = config['env_vars']

  opts = []
  grep = None
  services = []
  customOpts = [
    "--no-follow",
    "--grep",
    "-g",
  ]
  skipArgI = 0
  i = 0
  for arg in args:
    if skipArgI:
      skipArgI -= 1
      continue
    if arg[0:1] == "-":
      if arg not in customOpts:
        opts.append(arg)
      else:
        if arg == "--grep" or arg == "-g":
          grep = args[i+1]
          skipArgI += 1
    else:
      services.append(arg)
    i += 1

  cwd = os.getcwd()
  if len(services) == 0:
    for stack in stacks:
      stack_path = stack['path']
      os.chdir(stack_path)
      dir_env = copy.copy(env_vars)
      environ = config['environ'].copy()
      load_env_defaults(dir_env, environ)
      load_env_files(env_vars=dir_env)
      append_service = subprocess.check_output([
        'docker','stack','services',dir_env['STACKD_STACK_NAME'],
        '--format', '{{.Name}}',
      ], stderr=subprocess.DEVNULL).decode("utf-8").strip().split("\n")
      if append_service[0] != "":
        services = services + append_service
      os.chdir(cwd)

  if "-f" not in opts and "--follow" not in opts and "--no-follow" not in args:
    opts.append("-f")

  services_logs(services, opts, grep=grep)
