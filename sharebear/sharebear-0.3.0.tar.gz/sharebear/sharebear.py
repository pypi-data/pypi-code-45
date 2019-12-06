import yaml
import traceback
import random
import os.path
import argparse
from getpass import getuser

from shutil import move
import time
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader as Loader
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper
# the path to this script
this_script_path = os.path.realpath(__file__)
# the directory this script is located in
this_script_dir = os.path.dirname(this_script_path)
# the current user running this script
user = getuser()
# the global data object (a yaml file) to be stored or read from this script.
globals_yaml = os.path.join(this_script_dir, user + '.yaml')


def get_var(global_var, text_file=globals_yaml, fail_silently=False):
    """
    This function collects a keyed value from a yaml file and returns it to the user.
    :param global_var: the key of the global value you wish to collect
    :param text_file: the yaml file that the global variables are stored in, defaulted to global_vars.yaml
    :return: The global value variable, if there is no value due to either a key error or a file not found error it
    will return None.
    """
    try:
        with open(text_file, 'r') as infile:
            collected_globals = yaml.load(infile, Loader=Loader)
        global_var_value = collected_globals[global_var]
        return global_var_value
    except (FileNotFoundError, FileNotFoundError, KeyError):
        if fail_silently:
            pass
        else:
            traceback.print_exc()
        return None


def set_var(global_var, update_value, text_file=globals_yaml, delete=False):
    """
    This method checks the 'global' space for a value or updates the global space to have the update value it is
    provided. Global space is defined as a text file adjacent to this module that contains all  of the global variables
    one wishes to pass around for this project.
    :param global_var: the global variable you wish to either instantiate or update.
    :param update_value: the value with which you wish to assign to the global_var can be any type, I think.
    :param text_file: the default text file (aka 'global' space to write these values to) can be changed but defaults
    to a text file adjacent to this script defined in the globals_yaml variable
    :param delete by default this method creates a new variable or updates a variable stored in the global space,
    if the
    :return:
    """
    update_existing_file = False
    # first check to see if a file with variable exists, if not open one and write our desired global var to it
    try:
        with open(text_file, 'r') as infile:
            infile.close()
        # a file already exists so set update_existing_file to True to proceed to update logic below
        update_existing_file = True
    except FileNotFoundError:
        with open(text_file, 'w') as outfile:
            if not delete:
                global_vars = {}
                global_vars[global_var] = update_value
                yaml.dump(global_vars, outfile, Dumper=Dumper)
                return True
            else:
                print("Variable {} does not exist at {}, check to see if yaml file exists.".format(global_var, text_file))
                return False

    # Update existing yaml
    if update_existing_file:
        try:
            # collect data already in file
            with open(text_file, 'r') as infile:
                globals = yaml.load(infile, Loader=Loader)
                # if we open an empty file we need to initialize globals to an empty dict.
                if globals is None:
                    globals = {}
                if not delete:
                    globals[global_var] = update_value
                elif delete:
                    try:
                        var_exists = globals[global_var]
                        del globals[global_var]
                    except KeyError:
                        print("{} not found in {} global space.".format(update_value, text_file))
                        return False
            # make a tempfile to write old data + new data to
            temp_file = text_file + str(random.randint(0, 9999))
            with open(temp_file, 'w') as outfile:
                start_time = time.time()
                yaml.dump(globals, outfile, Dumper=Dumper)
                print('time to dump yaml: ', time.time() - start_time)
            # keep track of successful writing of data to temp file by comparing to globals dictionary
            success_write_temp = False
            with open(temp_file, 'r') as infile:
                temp_globals = yaml.load(infile, Loader=Loader)
                if temp_globals == globals:
                    # if data was successfully written to file mark success as true
                    success_write_temp = True

            # Overwrite text file with temp file if all has gone well.
            if success_write_temp:
                move(temp_file, text_file)
                return True
            else:
                print("IOError with updating global variable in {}".format(os.path.basename(this_script_path)))
                return False

        except (FileNotFoundError, FileExistsError):
            # if something bad happens throw up some errors to console, but don't crash.
            traceback.print_exc()
            return False


def del_var(global_var, text_file=globals_yaml, update_value=None):
    """
    Simple wrapper for set_var that passes delete argument as true.
    :param global_var: the var to delete
    :param text_file: the text file/yaml file to delete the value from
    :param update_value: this is set to None type because it doesn't matter since it's being deleted.
    :return:
    """
    status = set_var(global_var, update_value, text_file, delete=True)
    return status


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=
                                     """
                                     Provides a global space to store variables/python objects. Objects are stored
                                     in a yaml file then accessed, deleted, or updated by specifying the proper key
                                     and/or yaml file that they are stored in. Default behavior is to store all entries
                                     into a text file adjacent to where this script lives in the format <user>.yaml
                                     """)

    parser.add_argument('-s', '--set', metavar='SET', type=str, nargs=2,
                        help='Key value of data you wish to set/push/update in global space.')
    parser.add_argument('-g', '--get', metavar='GET', type=str,
                        help='Value to store under key specified by -g or --get')
    parser.add_argument('-d', '--delete', metavar='DELETE', type=str,
                        help='Key value you wish to delete from global space.')
    parser.add_argument('-y', '--yaml', metavar='YAMLFILE', type=str,
                        help='''
                        If you wish to access a particular global space (yaml file) or instantiate a new one
                        you need to supply a path to a file when using any of the above arguments. Otherwise YAMLFILE
                        will default to <user>.yaml at {}, specifically {}
                        '''.format(this_script_dir, globals_yaml))

    args = parser.parse_args()

    if args.set and not args.get and not args.delete:
        if args.yaml:
            yaml_file = args.yaml
        else:
            yaml_file = globals_yaml
        set_var(args.set[0], args.set[1], text_file=yaml_file)
    elif (args.set and args.get) or (args.set and args.delete):
        print("Please select only one action to perform (either --set --get or --delete.")

    if args.get and not args.set and not args.delete:
        if args.yaml:
            yaml_file = args.yaml
        else:
            yaml_file = globals_yaml
        if get_var(args.get, fail_silently=True) is None:
            print("{} not found in {}.".format(args.get, yaml_file))
        else:
            print(get_var(global_var=args.get, text_file=yaml_file, fail_silently=True))
    elif (args.get and args.set) or (args.get and args.delete):
        print("Please select only one action to perform (either --set --get or --delete.")

    if args.delete and not args.set and not args.get:
        if args.yaml:
            yaml_file = args.yaml
        else:
            yaml_file = globals_yaml
        status = del_var(global_var=args.delete, text_file=yaml_file)
        if status:
            print("{} was deleted from {}".format(args.delete, yaml_file))

