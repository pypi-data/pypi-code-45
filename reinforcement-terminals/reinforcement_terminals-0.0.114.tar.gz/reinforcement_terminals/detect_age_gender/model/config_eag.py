import yaml
import os
import pkgutil

path = 'detect_age_gender/model/config.yml'  # always use slash
filepath = pkgutil.get_data(__name__, path)

def get_config():
    with open(filepath, 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    return cfg
    

