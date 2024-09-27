#! /usr/bin/env python3

import argparse

# function to receive and parse command-line arguments
def get_args():
	# get input from the user, in this case the position in the 
	# Fib sequence that we're going to return
	# number = int(input("Enter the number: "))

	# create an argument parser object
	parser = argparse.ArgumentParser(description = 'This script \
		calculates the number in a specified position in the \
		Fibonacci sequence')

	# add positional (i.e., required) arguments
	parser.add_argument("position", help = "position in the Fibonacci \
		sequence", type = int)

	# add optional arguments
	# if 'store_true', this means to assign 'True' if the argument is
	# specified on the command line, so the default here for
	# 'store_true' is false
	parser.add_argument("-v", "--verbose", help = "Verbose output", \
		action = 'store_true')

	# parse the actual arguments
	args = parser.parse_args()

	# return the final output (the 'args' object)
	return args


# function to do the calculation
def fib(n):
	# initiate the sequence with 2 variables
	a,b = 0,1

	# initiate a list to store the fib numbers
	seq = [str(a)]

	for i in range(n-1):
		a,b = b,a+b
		seq.append(str(a))

	fibonacci_sequence = ",".join(seq)
	fibonacci_number   = a

	return fibonacci_sequence, fibonacci_number


# function to print the output, based on what the user asked for
def print_output(seq, num, position, verbose):

	if verbose:
		print(f'The Fibonacci sequence: {seq}')
		print(f'The Fibonacci number for {position} is: {num}')
	else:
		print(num)


# the main function
def main():
	fib_seq, fib_num = fib(arguments.position)
	print_output(fib_seq, fib_num, arguments.position, arguments.verbose)


# get the command-line arguments
arguments = get_args()



# set the environment for this script
# is this main (like a stand-alone script), or is this a module being called
# by another script
if __name__ == '__main__':
	main()



