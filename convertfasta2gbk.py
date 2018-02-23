#!/usr/bin/python

import sys
from datetime import date
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.Alphabet import generic_dna, generic_protein, IUPAC

try:
   input_handle = open(sys.argv[1], "rU")
   output_handle = open(sys.argv[1]+".gbk", "w")
except:
   print ("For use on predicted gene fasta files originating from RAST")
   print ("Usage: python convertfastatogbk fastafile")
   raise SystemExit

seqs = []
sequences = list(SeqIO.parse(input_handle, "fasta", alphabet=generic_dna))
tod = date.today()
todayis = tod.strftime("%d-%b-%Y")
elems = todayis.split('-')
elems[1]=elems[1].upper()
todd = "{}-{}-{}".format(elems[0],elems[1],elems[2])

#asign generic_dna or generic_protein
for seq in sequences:
  seq.seq.alphabet = generic_dna
  record = seq
  end = len(seq.seq)
  start = 1
  feature=SeqFeature(FeatureLocation(start=start,end=end), type='CDS')
  feature.qualifiers["translation"]=seq.seq.translate()
  record.features.append(feature)
  record.annotations["date"]="{}".format(todd)
  seqs.append(record)

count = SeqIO.write(seqs, output_handle, "genbank")

output_handle.close()
input_handle.close()
print ("Converted {} records".format(count))
