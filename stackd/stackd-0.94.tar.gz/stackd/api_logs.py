import sys
import subprocess
import signal

from .flatten import flatten

from .run_shell import run_shell

from .load_env_files import load_env_files
from .services_logs import services_logs

def api_logs(config, args=[]):

  load_env_files(config)

  files_compose = config['files_compose']
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
      services.append(env_vars['STACKD_STACK_NAME']+'_'+arg)
    i += 1

  if len(services) == 0:
    services = subprocess.check_output([
      'docker','stack','services',env_vars['STACKD_STACK_NAME'],
      '--format', '{{.Name}}'
    ]).decode("utf-8").strip().split("\n")

  if "-f" not in opts and "--follow" not in opts and "--no-follow" not in args:
    opts.append("-f")

  services_logs(services, opts, grep=grep)


