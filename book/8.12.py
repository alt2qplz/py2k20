'''
8.12. Сэндвичи: напишите функцию, которая получает список компонентов сэндвича.
Функция должна иметь один параметр для любого количества значений, переданных при
вызове функции, и выводить описание заказанного сэндвича. Вызовите функцию три раза
с разным количеством аргументов.
'''

def sandwich(*components):
	'''Выводит все компоненты сендвича, которые были переданы'''
	print('Ваш сендвич будет состоять из: ')
	for component in components:
		print(f'\t- {component}')
	print()


sandwich('лук', 'курица')

sandwich('хлеб', 'индейка', 'салат')

sandwich('рыба')