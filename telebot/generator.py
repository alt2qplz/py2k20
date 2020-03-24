'''
Генерирует список из 4 НЕПОВТОРЯЮЩИХСЯ цифр (str) 

['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
'''


from random import randint

def get_number():
	'''возвращает четыре цифры'''
	number =''
	numbers = [i for i in range(0, 10)]

	for i in range(4):
		number += str(numbers.pop(randint(0, (len(numbers)-1))))

	return(number)