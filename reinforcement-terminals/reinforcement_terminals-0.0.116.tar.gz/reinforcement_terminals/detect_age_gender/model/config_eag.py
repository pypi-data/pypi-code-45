import yaml
import os
import pkgutil

print("This is os: {}".format(os.path.split(__file__)))

this_dir, this_filename = os.path.split(__file__)

path = this_dir+ "\\" + 'config.yml' 

def get_config():
    with open(path, 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    return cfg
    

