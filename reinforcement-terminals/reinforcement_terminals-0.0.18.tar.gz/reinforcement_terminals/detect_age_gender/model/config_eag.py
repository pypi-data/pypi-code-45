import yaml
import os


def get_config():
    try:
        with open('reinforcement_terminals/detect_age_gender/model/config.yml', 'r') as ymlfile:
            cfg = yaml.safe_load(ymlfile)
            return cfg
    except:
        raise ValueError("config.yml not found")

