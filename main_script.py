#! /usr/bin/env python3

# import all our modules here
import say_hello
import csv
import argparse

def main():
	name = input("Enter your name: ")
	say_hello.greeting(name)

	num = input("Enter a number: ")
	say_hello.square_it(int(num))

	first  = input("Enter first number in range: ")
	second = input("Enter second number in range: ")

	say_hello.get_number(int(first), int(second))

# set the environment for this script
# is this main (like a stand-alone script), or is this a module being called
# by another script
if __name__ == '__main__':
	main()
