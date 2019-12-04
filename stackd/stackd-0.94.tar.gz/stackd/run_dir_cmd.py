import sys
import os

from .api_env import api_env
from .api_infos import api_infos
from .api_getname import api_getname
from .api_deploy import api_deploy
from .api_rm import api_rm
from .api_ls import api_ls
from .api_ps import api_ps
from .api_help import api_help
from .api_compo import api_compo
from .api_compo_freeze import api_compo_freeze
from .api_pull import api_pull
from .api_getimagelist import api_getimagelist
from .api_deploy_with_portainer import api_deploy_with_portainer
from .api_rm_with_portainer import api_rm_with_portainer
from .api_config_prune import api_config_prune
from .api_build import api_build
from .api_bundle import api_bundle
from .api_logs import api_logs
from .api_vc import api_vc
from .api_clear import api_clear
from .api_reset import api_reset
from .api_exec import api_exec
from .api_sh import api_sh
from .api_bash import api_bash
from .api_update import api_update
from .api_upgrade import api_upgrade
from .api_cc import api_cc
from .api_reboot_docker import api_reboot_docker
from .api_stacks import api_stacks

from .load_env_defaults import load_env_defaults
from .printError import printError

main_api = {
  'env': lambda config, args: api_env(config),
  'infos': lambda config, args: api_infos(config),
  'getname': lambda config, args: api_getname(config),
  'deploy': lambda config, args: api_deploy(config, args),
  'up': lambda config, args: api_deploy(config, args),
  'rm': lambda config, args: api_rm(config, args),
  'remove': lambda config, args: api_rm(config, args),
  'ls': lambda config, args: api_ls(args),
  'ps': lambda config, args: api_ps(config, args),
  'compo': lambda config, args: api_compo(config),
  'compo-freeze': lambda config, args: api_compo_freeze(config),
  'pull': lambda config, args: api_pull(config),
  'getimagelist': lambda config, args: api_getimagelist(config),
  'deploy-with-portainer': lambda config, args: api_deploy_with_portainer(config, args),
  'rm-with-portainer': lambda config, args: api_rm_with_portainer(config, args),
  'config-prune': lambda config, args: api_config_prune(args),
  'logs': lambda config, args: api_logs(config, args),
  'build': lambda config, args: api_build(config, args),
  'bundle': lambda config, args: api_bundle(config),
  'vc': lambda config, args: api_vc(config),
  'cc': lambda config, args: api_cc(config),
  'clear': lambda config, args: api_clear(config),
  'reset': lambda config, args: api_reset(config, args),
  'exec': lambda config, args: api_exec(config, args),
  'sh': lambda config, args: api_sh(config, args),
  'bash': lambda config, args: api_bash(config, args),
  'update': lambda config, args: api_update(config, args),
  'upgrade': lambda config, args: api_upgrade(config,args),
  'reboot-docker': lambda config, args: api_reboot_docker(args),
  'stacks': lambda config, args: api_stacks(config, args),
}

def run_dir_cmd(cmd, args, environ):
  if(cmd=='help' or cmd=='h'):
    api_help()
  else:
    run_dir_cmd_api(cmd, args, environ)


def run_dir_cmd_api(cmd, args, environ):

  config = {
    'env_vars': {},
    'vars_data': {},
    'files_env': [],
    'files_compose_src': [],
    'files_compose': [],
    'files_build_compose_src': [],
    'files_build_compose': [],
    'files_vars': [],
    'environ': environ,
  }

  load_env_defaults(config['env_vars'], config['environ'])

  if(cmd not in main_api):
    printError('ERROR: unkown command "stackd ' + cmd + '"')
    api_help()
    sys.exit(1)

  main_api[cmd](config, args)