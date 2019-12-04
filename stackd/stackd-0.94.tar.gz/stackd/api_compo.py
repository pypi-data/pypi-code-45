from .docker_compose_config import docker_compose_config

from .load_env_files import load_env_files
from .load_bundle import load_bundle
from .load_hash_versions import load_hash_versions


def api_compo(config):

  load_env_files(config)
  load_bundle(config)
  load_hash_versions(config)

  out = docker_compose_config(config['files_compose'], no_interpolate=True, env=config['environ'])
  print(out)