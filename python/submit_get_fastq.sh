#!/bin/bash -l

# Load the tools
module load bioinfo-tools sratoolkit
# Process the arguments
acc=u2020012
out=/mnt/picea/projects/arabidopsis/mschmid/porcupine-network/raw
srr=$1

# Submit

sbatch -A $acc -o $out ./get_fastq.sh $srr -e $out/fastq.err