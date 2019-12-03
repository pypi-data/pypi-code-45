__version__ = '0.2.2'
import logging.config
import os

import yaml

with open(f"{os.path.abspath('.')}/superwise/resources/logger_config.yml", 'r') as f:
    log_cfg = yaml.safe_load(f.read())


logging.config.dictConfig(log_cfg)
logger = logging.getLogger('superwise')
