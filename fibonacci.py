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

print(f'The Fibonacci sequence: {",".join(seq)}')
print(f'The Fibonacci number for {args.position} is: {fibonacci_number}')



