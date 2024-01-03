import gzip
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

subject_fasta="/mnt/picea/storage/reference/Populus-tremula/v2.2/fasta/Potra02_genome_hardmasked.fasta.gz"

# Load the subject genome
with gzip.open(subject_fasta, "rt") as handle:
         subject_genome = SeqIO.to_dict(SeqIO.parse(handle, "fasta"))

# Extract the sequence based on coordinates
start = 8712854
end = 8717644
strand = '+'
contig ='chr6'
gene='Potra2n6c13821'

if strand == '+':
    extracted_sequence = subject_genome[contig].seq[start-1:end]
else:
    extracted_sequence = subject_genome[contig].seq[start-1:end].reverse_complement()

seq_record = SeqRecord(extracted_sequence, id=gene, description=contig+':'+str(end)+'-'+str(start))

# Save the extracted sequence to a file
with open("extracted_seq_chr6_Potra2n6c13821.fasta", "w") as file:
    SeqIO.write(seq_record,file,"fasta")
file.close()
