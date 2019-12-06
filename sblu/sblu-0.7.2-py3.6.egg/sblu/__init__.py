from __future__ import absolute_import
import logging

from .config import get_config
try:
    from .version import version
except ImportError:
    version = "0.0.0"  # If version.py hasn't been created yet, just default to 0.0.0

from path import Path

__version__ = version

CONFIG = get_config()
PRMS_DIR = Path(CONFIG['prms_dir'])

logging.getLogger(__name__).addHandler(logging.NullHandler())
