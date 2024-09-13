#! /usr/bin/env python3

# get input from the user, in this case the position in the 
# Fib sequence that we're going to return

number = int(input("Enter the number: "))

# initiate the sequence with 2 variables
a,b = 0,1

for i in range(number):
	# print(i)
	a,b = b,a+b

fibonacci_number = a

print(f'The Fibonacci number for {number} is: {fibonacci_number}')