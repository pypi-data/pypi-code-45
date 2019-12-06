
import re

# must contain 'elf_base' 
def dbg_pie(p, gdb_env):
    with open("/proc/{}/maps".format(p.pid), "r") as f:
        buf = f.read(30)
        real_elf_base = int(re.findall('([\da-fA-F]+)(-)', buf)[0][0], 16)
    gdb_cmd = ''
    for key, val in gdb_env.items():
        gdb_cmd += 'set ${}={}\n'\
            .format(key, hex(val - gdb_env['elf_base'] + real_elf_base))
    return gdb_cmd

