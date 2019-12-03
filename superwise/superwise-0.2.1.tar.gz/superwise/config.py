import os

import yaml

from project_root import PROJECT_ROOT


class Config:

    config_file_path = os.path.join(PROJECT_ROOT, "superwise", "resources", "config.yml")

    with open(config_file_path, 'r') as config_file:
        config = yaml.load(config_file)

    SW_HOST = os.getenv('SW_HOST', config['SW_HOST'])
