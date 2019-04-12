#!/usr/bin/python


import sys


handle_dna = open(sys.argv[1]+".fasta", 'r')
handle_non = open(sys.argv[1]+".fasta.gff", 'r')

phrase = "##FASTA"

outfile = open(sys.argv[1]+"_withdna.gff", 'w')

for line in handle_non:
    outfile.write("%s\n"%(line.rstrip()))

outfile.write("%s\n"%(phrase))

for lin in handle_dna:
    outfile.write("%s\n"%lin.rstrip())
