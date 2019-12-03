import os

import yaml


class Config:

    config_file_path = f"{os.path.abspath('.')}/superwise/resources/config.yaml"

    with open(config_file_path, 'r') as config_file:
        config = yaml.load(config_file)

    SW_HOST = os.getenv('SW_HOST', config['SW_HOST'])
