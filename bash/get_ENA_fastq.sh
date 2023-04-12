#!/usr/bin/env bash
#SBATCH -w franklin
#SBATCH -c 2
#SBATCH -t 1-00:00:00
#SBATCH -A u2022016

set -euxo pipefail

# Process the arguments
IDs=$1  # file with the SRA/ERA/DRA RUN IDs
out=

if [ ! -f $IDs ]; then
  abort "The argument needs to be a file with one column of SRR/ERR/DRR IDs"
fi

cat $IDs | while read line ; do
    files=($out/$line*)

    if [ ! -e "${files[0]}" ]; then
        echo "Retrieving FASTQ file(s) for ${line}..."

{
        wget -P $out "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/${line:0:6}/00${line: -1}/$line/*"
} || {
	wget -P $out "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/${line:0:6}/0${line: -2}/$line/*"
} || {
	wget -P $out "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/${line:0:6}/$line/*"
}

    fi
done
