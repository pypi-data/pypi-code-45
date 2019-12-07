import os
import logging
import configparser
import json


def get_appropriate_env_vars(prefix):
    """
    Given a prefix, return all applicable environment variables as a dict
    """
    ret = {}
    for name, value in os.environ.items():
        if name.startswith(prefix):
            short_name = name[len(prefix):]
            ret[short_name] = value
    return ret


def convert_vars_to_dict(env_vars):
    """
    Take a dict of processed env variables, and convert them to a python
    dictionary
    """
    ret = {}
    for name, value in env_vars.items():
        if "__" in name:
            section, option = name.split("__")
            if section not in ret:
                ret[section] = {}
            ret[section][option] = value
    return ret


def load_ini_file(reference_file):
    ret = {}
    c = configparser.ConfigParser()
    c.read_file(reference_file)
    for section in c.sections():
        ret[section] = {}
        for option in c.options(section):
            ret[section][option] = c.get(section, option)
    return ret


def write_ini_output_file(values, output_file):
    config = configparser.ConfigParser()
    for section, section_values in values.items():
        config[section] = {}
        for k, v in section_values.items():
            config[section][k] = v
    with open(output_file, 'w') as configfile:
        config.write(configfile)


def write_json_output_file(values, output_file):
    with open(output_file, 'w') as configfile:
        configfile.write(json.dumps(values))


def parse_env(*args, **kwargs):
    """
    Take ENV vars and conver them to a config file
    """
    prefix = kwargs.get('prefix')
    cfg_type = kwargs.get('cfg_type')
    output_file = kwargs.get('output_file')
    reference_file = kwargs.get('reference_file', None)

    environment_vars = get_appropriate_env_vars(prefix)

    # First off, load any existing config in to a dict
    existing_config = {}
    if reference_file and (cfg_type == 'ini'):
        existing_config = load_ini_file(reference_file)

    # Now overwrite with what we loaded from the env
    new_config = convert_vars_to_dict(environment_vars)
    existing_config.update(new_config)

    # Unsure if this is really needed but...
    final_config_values = existing_config
    del (existing_config)

    if cfg_type == 'ini':
        write_ini_output_file(final_config_values, output_file)
    elif cfg_type == 'json':
        write_json_output_file(final_config_values, output_file)
