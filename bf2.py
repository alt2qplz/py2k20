import string
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



def get_sim(simvol, spisok):
	'''Возвращает следующий символ из списка симоволов для пароля'''
	if simvol == '':
		simvol = spisok[0]
	elif simvol == my_pass[-1]:
		simvol = spisok[0]
	else:
		simvol = spisok[(spisok.index(simvol)) + 1]

	return(simvol)


print(my_pass)
print(get_sim('_', my_pass))

'''
x = 1

lucky_pass = get_pass(x)

print(lucky_pass)

bf_pass = []


for i in range(len(bf_pass)):
	bf_pass[i] = 5



print()
print(bf_pass)
print(i)

'''


