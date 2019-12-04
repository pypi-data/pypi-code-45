import sys
import subprocess

from .run_shell import run_shell

def run_shell_print(cmd):
  print(" ".join(cmd))
  return run_shell(cmd)

def api_reboot_docker(args=[]):

  process = run_shell_print([
    "sudo","/etc/init.d/docker","stop",
  ])
  process = run_shell_print([
    "sudo","su","root",'-c "umount /var/run/docker/netns/*"',
  ])
  process = run_shell_print([
    "sudo","su","root",'-c "rm /var/run/docker/netns/*"',
  ])

  ifaceLS = subprocess.check_output([
    'ip','link','show',
  ]).decode("utf-8").strip().split("\n")

  for iface in ifaceLS:
    parts = iface.split(" ")
    ifaceName = parts[1][0:-1]
    if ifaceName[0:3] == "vx-":
      process = run_shell_print([
        "sudo","ip","link","delete",ifaceName,
      ])

  process = run_shell_print([
    "sudo","/etc/init.d/docker","start",
  ])

  if(process.returncode != 0):
    sys.exit(process.returncode)
