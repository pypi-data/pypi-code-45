import os
import glob

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from .paths import get_bundle_j2_compose_file_path, ensure_build_dir_exists
from .get_template import get_template

from .build_stack_compose_dependencies import build_stack_compose_dependencies

def build_j2yml(name, env_vars={}, vars_data={}):
  j2 = name + '.j2.yml'
  template = get_template(j2)

  buildj2 = get_bundle_j2_compose_file_path(env_vars, name)

  rendered = template.render(vars_data)
  ensure_build_dir_exists(env_vars)
  with open(buildj2, "w") as fh:
    fh.write(rendered)


def add_compose_file(name, files_compose=[], env_vars={}, files_compose_src=[], vars_data={}):
  file = name + '.yml'
  file_j2 = name + '.j2.yml'
  if os.path.exists(file):
    files_compose.append(file)
    files_compose_src.append(file)
  elif os.path.exists(file_j2):
    build_j2yml(name, env_vars, vars_data)
    file = get_bundle_j2_compose_file_path(env_vars, name)
    files_compose.append(file)
    files_compose_src.append(file_j2)
  return files_compose

# MAKE DOCKER STACK COMPOSE FILES LIST AND COMPILE JINJA TEMPLATES
def load_compose(config):

  load_compose_files(
    config['env_vars']['STACKD_COMPOSE_FILE_BASE'],
    config['files_compose'],
    config['env_vars'],
    config['files_compose_src'],
    config['vars_data']
  )

  load_compose_files(
    config['env_vars']['STACKD_BUILD_COMPOSE_FILE_BASE'],
    config['files_build_compose'],
    config['env_vars'],
    config['files_build_compose_src'],
    config['vars_data']
  )

  common_dirs = config['env_vars']['STACKD_COMMON_DIRS'].split(',')
  cwd = os.getcwd()
  for common_dir in common_dirs:
    if common_dir != "":
      if common_dir[0:1] != "/":
        common_dir = cwd+"/"+common_dir
      for file in glob.glob(common_dir + '/*'):
        if file[-4:len(file)] == ".yml":
          name = file[0:-4]
        elif file[-7:len(file)] == ".j2.yml":
          name = file[0:-7]
        else:
          continue
        add_compose_file(name, files_compose=config['files_compose'], env_vars=config['env_vars'], vars_data=config['vars_data'])

def load_compose_files(
    file_base,
    files_compose=[],
    env_vars={},
    files_compose_src=[],
    vars_data={}
  ):
  addons_ls = env_vars['STACKD_ADDONS'].split(',')
  env_ls = env_vars['STACKD_ENV'].split(',')
  for compose_file_name in file_base.split(','):
    compose_base_name = os.path.splitext(compose_file_name)[0]

    add_compose_file(compose_base_name, files_compose, env_vars, files_compose_src, vars_data)

    for addon_key in addons_ls:
      add_compose_file(compose_base_name + '-' + addon_key, files_compose, env_vars, files_compose_src, vars_data)

    for env_key in env_ls:
      add_compose_file(compose_base_name + '.' + env_key, files_compose, env_vars, files_compose_src, vars_data)

    for addon_key in addons_ls:
      for env_key in env_ls:
        add_compose_file(compose_base_name + '-' + addon_key + '.' + env_key, files_compose, env_vars, files_compose_src, vars_data)

  build_stack_compose_dependencies(files_compose, env_vars)

