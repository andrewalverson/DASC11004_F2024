#! /usr/bin/env python3

import argparse
import gff_functions

def parse_args():
	# create an argument parser object
	parser = argparse.ArgumentParser(description = "This script \
	    parses a GFF file and extracts the genes from the \
	    corresponding genome.")

	# add positional arguments
	parser.add_argument("fasta", help = "genome sequence in FASTA format", type = str)
	parser.add_argument("gff", help = "GFF file", type = str)

	# parse the arguments
	return parser.parse_args()


def main():
	# parse the fasta file
	genome = gff_functions.read_fasta(args.fasta)

	# parse the GFF file
	gff_functions.read_gff(args.gff, genome)

# parse the arguments
args = parse_args()

# set the environment for this script
if __name__ == '__main__':
	main()