#See my webpage:
#http://www.warwick.ac.uk/go/peter_cock/python/genbank2fasta/
from Bio import SeqIO
import sys

gbk_filename = sys.argv[1]
fna_filename = sys.argv[2]

#gbk_filename = raw_input('which input file? ')
#fna_filename = raw_input('which output file? ')

input_handle  = open(gbk_filename, "r")
output_handle = open(fna_filename, "w")

#Short version:
#SeqIO.write(SeqIO.parse(input_handle, "genbank"), output_handle, "fasta")

#Long version, allows full control of fasta output
for seq_record in SeqIO.parse(input_handle, "genbank") :
    print("Dealing with GenBank record {}".format(seq_record.id))
    output_handle.write(">{} {}\n{}\n".format(
           seq_record.id,
           seq_record.description,
           str(seq_record.seq)))

output_handle.close()
input_handle.close()
print("Done")
