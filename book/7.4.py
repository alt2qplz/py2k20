'''
7.4. Топпинг для пиццы: напишите цикл, который предлагает пользователю вводить
дополнения для пиццы до тех пор, пока не будет введено значение 'quit'.
При вводе каждого дополнения выведите сообщение о том,
что это дополнение включено в заказ.
'''

topping = True

while topping:
	addTopping = input('Добавьте топиини для пиццы, или напишите quit '
		'для выхода: \n')
	if addTopping == 'quit':
		topping = False
		print('Ваш заказ принят')
	else:
		print(f'\nДобавлин топпинг для пиццы: {addTopping}\n')