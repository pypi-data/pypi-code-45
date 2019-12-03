import yaml
import os
import pkg_resources

path = 'config.yml'  # always use slash
filepath = pkg_resources.resource_filename(__name__, path)

def get_config():
    with open(filepath, 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    return cfg
    

