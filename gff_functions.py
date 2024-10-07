#! /usr/bin/env python3

import csv
import re

def read_fasta(fasta_file):
	# make a variable to store our DNA sequence
	dna_sequence = ''

	# open file
	with open(fasta_file, 'r') as infile:
		# skip the first (header) line
		next(infile)
		for line in infile:
			dna_sequence += line.strip()

	# print(dna_sequence)
	# print(len(dna_sequence))

	# return the DNA sequence string
	return dna_sequence

def read_gff(gff_file, genome_sequence):
	# open the file for reading
	with open(gff_file, 'r') as gff:

		# create a csv reader object
		reader = csv.reader(gff, delimiter='\t')
    
		# loop over lines in the reader object
		for line in reader:
			start   = int(line[3])
			end     = int(line[4])
			feature = line[8]

			# extract the sequence for this feature/gene
			seq = genome_sequence[start-1:end]

			# extract the sequence header
			a = feature.split(';')
			id_field = a[0]

			id = re.compile("ID=(.*)")
			match = re.search(id, id_field)
			header = match.group(1)
			
			write_output(seq, header)			

def write_output(seq, header):
	# print the header line
	print('>' + header)
	print(seq)







