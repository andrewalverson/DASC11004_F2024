#! /usr/bin/env python3

import random
import string

# ask user for password length
pass_length = int(input("Enter the length of your password: "))

#print(string.ascii_letters)
#print(string.ascii_lowercase)
#print(string.digits)
#print(string.punctuation)

# make a big string of letters, numbers, and punctuation marks
# we'll draw from this to make our password
characters = string.ascii_letters + string.digits + \
string.punctuation + string.ascii_lowercase

# print(characters)

print()

for i in range(pass_length):
	print(random.choice(characters), end = '')

print()

# another way to do it

# make an empty string to hold the password
password = ''

for i in range(pass_length):
	password += random.choice(characters)

print(password)

