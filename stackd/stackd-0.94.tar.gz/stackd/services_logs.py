import subprocess

from .multiprocess_loop import multiprocess_loop
from .run_shell import run_shell

def services_logs(services, opts={}, grep=None):
  service_defs = []
  for service in services:
    if service != "":
      service_defs.append([service, opts, grep])

  log_pool(service_defs)

def log_service(service_def):
  service_name, opts, grep = service_def
  if grep is not None:
    if '--color=' not in grep:
      grep += " --color=always"
    cmd = ['docker','service','logs',opts,service_name,"2>&1","|","grep",grep]
    cmd = flatten(cmd)
    cmd = ' '.join(cmd)
    subprocess.run(cmd, shell=True, stdin=subprocess.PIPE)
  else:
    run_shell(['docker','service','logs',opts,service_name])

def log_pool(service_defs):
  multiprocess_loop(log_service, service_defs)
