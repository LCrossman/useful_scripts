#!/usr/bin/python


import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.SeqRecord import SeqRecord
from BCBio import GFF
from datetime import date


try:
    handle = open(sys.argv[1], 'r')
except:
    print("Usage: python GFF2gbk.py filename")


i=0
sequences = []
tod = date.today()
todayis = tod.strftime("%d-%b-%Y")
print(todayis.upper())

for rec in GFF.parse(handle):
    i +=1
    outfile = open(sys.argv[1]+str(i)+".gb", 'w')
    if rec.id > 20:
        newid = rec.id[:20]
    else:
        newid=rec.id
    new_rec = SeqRecord(Seq(str(rec.seq), generic_dna), id=newid, description=rec.description)
    new_rec.annotations["date"]=todayis.upper()
    print(new_rec.annotations)
    for feature in rec.features:
        new_rec.features.append(feature)
    SeqIO.write(new_rec, outfile, "genbank")

