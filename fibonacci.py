#! /usr/bin/env python3

import argparse

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
parser.add_argument("-b", "--beyonce", help = "Verbose output for\
	Beyonce", action = 'store_true')


# parse the actual arguments
args = parser.parse_args()


# initiate the sequence with 2 variables
a,b = 0,1

# initiate a list to store the fib numbers
seq = [str(a)]

for i in range(args.position-1):
	a,b = b,a+b
	seq.append(str(a))

fibonacci_number = a

# print the output, based on what the user asked for

if args.verbose:
	print(f'The Fibonacci sequence: {",".join(seq)}')
	print(f'The Fibonacci number for {args.position} is: {fibonacci_number}')
elif args.beyonce:
	print(f'Beyonce, the Fibonacci sequence: {",".join(seq)}')
	print(f'Beyonce, the Fibonacci number for {args.position} is: {fibonacci_number}')
else:
	print(fibonacci_number)


