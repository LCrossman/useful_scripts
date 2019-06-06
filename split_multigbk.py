#!/usr/bin/python


import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

handle = open(sys.argv[1], 'r')

records = list(SeqIO.parse(handle, "genbank"))

for rec in records:
    fil = str(rec.id)+".gbk"
    print(type(fil))
    outfile = open(fil, 'w')
    SeqIO.write(rec, outfile, "genbank")
