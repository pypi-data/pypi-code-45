import json

from .get_required_images import get_required_images

from .load_env_files import load_env_files
from .load_bundle import load_bundle
from .load_hash_versions import load_hash_versions

def api_getimagelist(config):

  load_env_files(config)
  load_bundle(config)
  load_hash_versions(config)

  print(json.dumps(list(get_required_images(config['files_compose']))))