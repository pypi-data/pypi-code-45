import toml
from pathlib import Path


path_to_config = (Path(__file__) / '../config.toml').resolve()
_config = toml.load(path_to_config)


def __getattr__(key):
    return _config[key]
