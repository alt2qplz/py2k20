'''
Генерирует список символов состящий из всех цифр, буква латинского алвфавита
в обоих регистрах и символа '_'

['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 
'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']
'''

import string

def password_list():
	'''Возвращает набор символов для составления пароля'''
	my_pass = [i for i in range(0, 10)]

	for i, elem in enumerate(my_pass):
	    my_pass[i] = str(elem)

	my_pass.extend(list(string.ascii_letters))

	my_pass.append('_')

	return(my_pass)