import os

def load_env_defaults(env_vars, environ):
  env_vars['STACKD_STACK_NAME'] = environ.get('STACKD_STACK_NAME') or os.path.basename(os.getcwd())
  env_vars['STACKD_COMPOSE_FILE_BASE'] = environ.get('STACKD_COMPOSE_FILE_BASE') or "docker-stack.yml"
  env_vars['STACKD_ADDONS'] = environ.get('STACKD_ADDONS') or ""
  env_vars['STACKD_COMMON_DIRS'] = environ.get('STACKD_COMMON_DIRS') or ""
  env_vars['STACKD_BUNDLE_DIR'] = environ.get('STACKD_BUNDLE_DIR') or ".stackd-bundle"
  env_vars['STACKD_BUILD_COMPOSE_FILE_BASE'] = environ.get('STACKD_BUILD_COMPOSE_FILE_BASE') or "docker-compose.yml"
  env_vars['STACKD_VARS_FILE_BASE'] = environ.get('STACKD_VARS_FILE_BASE') or "vars.yml"
  env_vars['STACKD_ENV'] = environ.get('STACKD_ENV') or ""
  env_vars['STACKD_DEPLOY_PULL_CHECK'] = environ.get('STACKD_DEPLOY_PULL_CHECK') or "true"
  env_vars['STACKD_DEPLOY_WITH_REGISTRY_AUTH'] = environ.get('STACKD_DEPLOY_WITH_REGISTRY_AUTH') or "true"
  env_vars['STACKD_DEPLOY_PRUNE'] = environ.get('STACKD_DEPLOY_PRUNE') or "true"
  env_vars['STACKD_DEPLOY_PARAMETERS'] = environ.get('STACKD_DEPLOY_PARAMETERS') or ""
  env_vars['STACKD_BUILD_PARAMETERS'] = environ.get('STACKD_BUILD_PARAMETERS') or ""
  STACKD_MACHINE_ID = environ.get('STACKD_MACHINE_ID')

  if not STACKD_MACHINE_ID:
    with open('/var/lib/dbus/machine-id', 'r') as content_file:
      STACKD_MACHINE_ID = content_file.read().strip()
  env_vars['STACKD_MACHINE_ID'] = STACKD_MACHINE_ID
  env_vars['STACKD_DEV_TAG'] = environ.get('STACKD_DEV_TAG') or "dev-"+STACKD_MACHINE_ID