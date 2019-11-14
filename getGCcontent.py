#!/usr/bin/python3


from Bio import SeqIO
from Bio.SeqUtils import GC
import sys


handle = open(sys.argv[1], 'r')

records = list(SeqIO.parse(handle, "fasta"))

sequences = []

for rec in records:
    print("{}\t{}".format(rec.id, GC(rec.seq)))
