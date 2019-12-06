"""Console script for sharebear."""
import argparse
import sys
from sharebear.sharebear import *


def main():
    """Console script for sharebear."""
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

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
