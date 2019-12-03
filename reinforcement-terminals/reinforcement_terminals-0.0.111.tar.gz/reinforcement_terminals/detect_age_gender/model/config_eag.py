import yaml
import os


def get_config():
    with open('model/config.yml', 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    return cfg
    

