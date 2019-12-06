from Bio import SeqIO
from Bio import Entrez
import Bio as b

Entrez.email = 'jhmdf@hotmail.com'

handle = Entrez.esearch(db='gene', term='Human[Orgn] AND FANCF[gene]')
rec = Entrez.read(handle)
rec['IdList']
# print(rec['IdList0])
# >>>['3020', '3021']

# from here, you should look for the results you have, preferably with a for cycle and
# check the name to match yours H3-3B
handle = Entrez.efetch(db='gene', id='2188', rettype = 'gb', retmode = 'text')#, retmode='xml')
handle2 = Entrez.efetch(db='nuccore', id = 'NC_000011.10', seq_start = 22622533, seq_stop = 22625823, retmode = 'xml')

records = Entrez.read(handle)

d  # <- this is a dictionary, you should iterate over this to
