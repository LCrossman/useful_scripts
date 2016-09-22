#!/usr/bin/python

from __future__ import division
import sys
import math
from Bio.Seq import Seq
from Bio import SeqIO
from Bio import AlignIO
from Bio.Align import AlignInfo
from Bio.Alphabet import IUPAC, Gapped
from Bio.SeqRecord import SeqRecord
alphabet = Gapped(IUPAC.ambiguous_dna)
flag = 0

try:
    handle = open(sys.argv[1], 'r')
except:
    print "Usage: python create_consensus.py filename of multiple sequence alignment in fasta format"



def trim_consensus(alignment):
    flag = 0
    front_str = alignment[:, 0]
    print "First character for potential trimming:%s"%front_str
    back_str = alignment[:, -1]
    print "Last character for potential trimming:%s"%back_str
    fs = front_str.count('-')
    bs = back_str.count('-')
    print len(front_str), (len(front_str)/3), fs, bs, flag
    if fs > (len(front_str)/3):
        new_align = alignment[:, 1:]
        print "trimming first character"
        if bs > (len(back_str)/3):
            new_align = new_align[:, :-1]
            print "trimming last character"
            flag = 1
    if bs > (len(back_str)/3) and flag < 1:
        new_align = alignment[:, :-1]
        print "trimming last character but not first"
    return new_align

alignment = AlignIO.read(handle, "fasta")

clean_align = trim_consensus(alignment)
print clean_align
summary_align = AlignInfo.SummaryInfo(clean_align)

gap_consensus = summary_align.gap_consensus(threshold = 0, ambiguous = 'N', consensus_alpha=alphabet, require_multiple=1)

dumb_consensus = summary_align.dumb_consensus(threshold = 0, ambiguous = 'N', consensus_alpha=alphabet, require_multiple = 1)

outfile_gap = open(sys.argv[1]+"_gap_consensus.fasta", "w")
outfile_dumb = open(sys.argv[1]+"_dumb_consensus.fasta", "w")
outfile_ungap = open(sys.argv[1]+"_ungap_consensus.fasta", "w")

ungap_consensus = gap_consensus.ungap("-")

SeqIO.write(SeqRecord(gap_consensus, id="%s"%(sys.argv[1]+"_gap_consensus"), description=""), outfile_gap, "fasta")
SeqIO.write(SeqRecord(dumb_consensus, id="%s"%(sys.argv[1]+"_dumb_consensus"), description=""), outfile_dumb, "fasta")
SeqIO.write(SeqRecord(ungap_consensus, id="%s"%(sys.argv[1]+"_ungap_consensus"), description=""), outfile_ungap, "fasta")
