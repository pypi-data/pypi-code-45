import os

def get_bundle_j2_compose_file_path(env_vars, name):
  return env_vars['STACKD_BUNDLE_DIR'] + '/' + env_vars['STACKD_STACK_NAME'] + '.' + name + '.j2.yml'

def get_bundle_stack_compose_file_path(env_vars):
  return env_vars['STACKD_BUNDLE_DIR'] + '/' + env_vars['STACKD_STACK_NAME'] + '.stack.yml'

def get_bundle_stack_env_file_path(env_vars):
  return env_vars['STACKD_BUNDLE_DIR'] + '/' + env_vars['STACKD_STACK_NAME'] + '.env'

def ensure_build_dir_exists(env_vars):
  build_dir = env_vars['STACKD_BUNDLE_DIR']
  if not os.path.exists(build_dir):
    os.makedirs(build_dir)