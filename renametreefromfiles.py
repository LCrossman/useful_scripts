#!/usr/bin/python

#script for renaming phylogenetic trees with a new label.  Provide a file with two columns separated by tabs.  First column is the current label.  Second column is the new label
#resulting file has newlines which can be removed with perl -pe 's/\n//g' and redirecting the file to a new filename
import sys
import re

infile = open(sys.argv[1], 'r')

namesfile = open(sys.argv[2], 'r')

d = {}

for line in namesfile:
    elements = line.rstrip().split()
    taxid = elements[0]
    specname = elements[1]
    try:
        d[taxid].append(specname)
    except:
        d[taxid]=specname

for line in infile:
        items = [lin.rstrip() for lin in re.split(r'([^:,\(\) ]+)',line)]
        for it in items:
           if it in d.keys():
                print(d[it])
           else:
                print(''.join(it))
