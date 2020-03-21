def get_sim(simvol, spisok):
	'''Возвращает следующий символ из списка симоволов для пароля'''
	if simvol == '':
		simvol = spisok[0]
	elif simvol == my_pass[-1]:
		simvol = spisok[0]
	else:
		simvol = spisok[(spisok.index(simvol)) + 1]

	return(simvol)