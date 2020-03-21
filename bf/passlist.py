import string

def password_list():
	'''Возвращает набор символов для составления пароля'''
	my_pass = [i for i in range(0, 10)]

	for i, elem in enumerate(my_pass):
	    my_pass[i] = str(elem)

	my_pass.extend(list(string.ascii_letters))

	my_pass.append('_')

	return(my_pass)