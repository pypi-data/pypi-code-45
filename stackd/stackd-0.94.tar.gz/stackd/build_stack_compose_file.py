from .docker_compose_config import docker_compose_config
from .paths import ensure_build_dir_exists, get_bundle_stack_compose_file_path

def build_stack_compose_file(config):
  yaml_dump = docker_compose_config(config['files_compose'], no_interpolate=True, env=config['environ'])
  compose_file = get_bundle_stack_compose_file_path(config['env_vars'])
  ensure_build_dir_exists(config['env_vars'])
  f = open(compose_file, 'w+')
  f.write(yaml_dump)
  f.close()