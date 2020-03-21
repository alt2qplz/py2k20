'''
Перебор элементов списка по очереди
'''

def get_sim(simvol, spisok):
	'''Возвращает следующий элемент из списка'''
	if simvol == '':
		simvol = spisok[0]
	elif simvol == spisok[-1]:
		simvol = spisok[0]
	else:
		simvol = spisok[(spisok.index(simvol)) + 1]

	return(simvol)