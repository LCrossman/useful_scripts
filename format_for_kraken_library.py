#!/usr/bin/python3


#requires biopython

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


try:
    with open(sys.argv[1], 'r') as handle:
        records = list(SeqIO.parse(handle, "fasta"))
except:
    print("Usage: format_for_kraken_library.py fastafile")


sequences = []
i = 0


for rec in records:
       short = rec.id
       newid = "{}|kraken:taxid|{}".format(id,i)
       new_rec = SeqRecord(rec.seq, id=newid, description="")
       sequences.append(new_rec)
       i+=1
    else:
        print("formatting issue", rec.id)


outfile = open(sys.argv[1]+"formatted_for_kraken_library.fasta", 'w')
SeqIO.write(sequences, outfile, "fasta")
