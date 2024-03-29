#!/bin/bash

# Get SRA ids (first column) from SraRunTable.txt file
SRA=$(tail -n +2 SraRunTable.txt | cut -d ',' -f 1)

# This is a loop for downloading the data files
for i in ${SRA}
    do
        echo "(*) Downloading SRA entry: ${i}"
        prefetch ${i}
        echo "(*) Dumping to fastq ${i}"
        fastq-dump ${i}
    done
