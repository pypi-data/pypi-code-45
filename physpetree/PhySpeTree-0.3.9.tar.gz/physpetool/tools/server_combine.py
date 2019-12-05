import os
proindexlist = [['ath:AT2G27530', 'zma:103638688', 'eco:b3984'], ['ath:ArthCp055', 'zma:845224', 'eco:b3295']]

db_dir ="/home/yangfang/PhySpeTree/revision/HCPDB/databasehcp/"
tem_dir = "/home/yangfang/PhySpeTree/revision/HCPDB/tem/"
if not os.path.isdir(tem_dir):
    os.mkdir(tem_dir)

p=1
for line in proindexlist:
    res = []
    for each in line:
       with open(db_dir+each + ".fasta") as f:
           tem = f.read().split("\n")
           tem[0] = tem[0].strip().split(":")[0]
           res.append("\n".join(tem) + "\n")
    w_path = open(tem_dir+ "p" + str(p) + ".fasta",'w')
    w_path.write("".join(res))



####deal with hcp db

db_dir = "/home/yangfang/PhySpeTree/revision/HCPDB/databasehcp_backup/"

w_dir = "/home/yangfang/PhySpeTree/revision/HCPDB/databasehcp/"

test =  []
with open("/home/yangfang/PhySpeTree/physpetools/physpetool/database/support_hcp_organism.txt") as f:
    for line in f:
        test.append(line.strip().split("\t")[0])



all_files = list(filter(lambda f: not f.startswith('.'), os.listdir(db_dir)))
s = set()
for line in all_files:
    abb_name = line.strip().split(":")[0]
    s.add(abb_name)

    # w_ = open(w_dir+abb_name+".fasta",'a')
    # seq_file = open(db_dir+line)
    # seq = seq_file.read()
    # w_.write(seq+"\n")
    # seq_file.close()
    # w_.close()


