import string
from random import choice





def get_pass(list, sim=3):
	'''возвращает пароль длинной sim из списка символов list'''
	password =''

	for i in range(sim):
		password += str(choice(list))

	return(password)