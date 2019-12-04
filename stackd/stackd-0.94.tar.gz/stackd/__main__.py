import sys
import os

from .split_list import split_list

from .run_dir_cmd import run_dir_cmd

def main():
  argsList=sys.argv.copy()
  cws=argsList.pop(0)
  argsList = split_list(argsList, "--")

  if len(argsList) == 0:
    argsList.append(["help"])

  env_origin = os.environ.copy()

  for args in argsList:
    cmd=args.pop(0) if len(args) > 0 else 'help'
    run_dir_cmd(cmd, args, environ=env_origin)

if __name__ == '__main__':
  main()