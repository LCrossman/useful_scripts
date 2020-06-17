#!/usr/bin/python

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature
import sys

try:
   handle = open(sys.argv[1], 'r')
except:
   print("Usage: python convert_gbk_to_UCSC-type_bed.py genbankfile > output.bed")

records = list(SeqIO.parse(handle, "genbank"))

for rec in records:
    chr = rec.id
    for feature in rec.features:
        if feature.type == "CDS":
            start = feature.location.start
            end = feature.location.end
            strand = feature.location.strand
            if strand > 0:
                strand = '+'
            else:
                strand = '-'
            citation = 4
            locustag = ''.join(feature.qualifiers['locus_tag'])
            try:
                gene = ''.join(feature.qualifiers['gene'])
            except:
                gene = locustag
            product = ''.join(feature.qualifiers['product'])
            tagnum = locustag.split('_')
            numtag = tagnum[-1]
            print("{}\t{}\t{}\t{}\t4\t{}\t{}\t{}\tprotein-coding\t{}\t{}\t{}\t{}\t{}".format(chr,start,end,gene,strand,locustag,numtag,product,start,end,start,end))
