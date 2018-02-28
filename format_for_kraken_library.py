#!/usr/bin/python3


#requires biopython

import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


try:
    handle = open(sys.argv[1], 'r')
except:
    print("Usage: format_for_kraken_library.py fastafile")


records = list(SeqIO.parse(handle, "fasta"))
sequences = []
i = 0


for rec in records:
    try:
       short = rec.id
       newid = "{}|kraken:taxid|{}".format(rec.id,i)
       new_rec = SeqRecord(rec.seq, id=newid, description="")
       sequences.append(new_rec)
       i+=1
    except:
        print("formatting issue", rec.id)


outfile = open(sys.argv[1]+"formatted_for_kraken_library.fasta", 'w')
SeqIO.write(sequences, outfile, "fasta")
