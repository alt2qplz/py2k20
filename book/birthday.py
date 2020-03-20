with open('res/pi_million_digits.txt') as file_object:
	pi = file_object.readlines()

pi_string = ''

for line in pi:
	pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")
