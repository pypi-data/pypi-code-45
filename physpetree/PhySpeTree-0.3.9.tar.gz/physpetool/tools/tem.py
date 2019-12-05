import os

read_dir = "/home/yangfang/PhySpeTree/revision/HCPDB/hcp_append/"
write_dir = "/home/yangfang/PhySpeTree/revision/HCPDB/hcp_append_trans/"

all_files = list(filter(lambda f: not f.startswith('.'), os.listdir(read_dir)))

for line in all_files:
    oldname = read_dir + line
    newname = read_dir + line[1:]
    os.rename(oldname, newname)