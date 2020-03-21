import string
import sys
import os
from random import choice

abc = list(string.ascii_letters)


my_pass = [i for i in range(0, 10)]
for i, elem in enumerate(my_pass):
    my_pass[i] = str(elem)


my_pass.extend(abc)

my_pass.append('_')

def get_pass(sim):

	password =''

	for i in range(sim):
		password += str(choice(my_pass))

	return(password)


x = 3

lucky_pass = get_pass(x)

print(lucky_pass)

bf_pass = get_pass(x)

i = 1

while bf_pass != lucky_pass:
	bf_pass = get_pass(x)
	i += 1
	print(i, end='\r')

print()
print(bf_pass)
print(i)