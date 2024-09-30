#! /usr/bin/env python3

import random

# this is a module
# this script is all functions, but importantly no main() function

def greeting(input_name):
	print(f'Hello, {input_name}, it\'s good to see you')

def square_it(num):
	print(f'{num} squared is equal to: {num*num}')

def get_number(a,b):
	rand = random.randint(a, b)
	print("Your random number is:", rand)

# set the environment for this script
# is this main (like a stand-alone script), or is this a module being called
# by another script
if __name__ == '__main__':
	main()
