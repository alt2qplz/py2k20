import random

def random_card():
	# Получение случайной карты из словаря
	cards = {
		'ТУЗ':'11', 
		'ДВОЙКА':'2',
		'ТРОЙКА':'3',
		'ЧЕТВЕРКА':'4',
		'ПЯТЕРКА':'5',
		'ШЕСТЕРКА':'6',
		'СЕМЕРКА':'7', 
		'ВОСЬМЕРКА':'8',
		'ДЕВЯТКА':'9', 
		'ДЕСЯТКА':'10', 
		'ВАЛЕТ':'10', 
		'ДАМА':'10', 
		'КОРОЛЬ':'10'
		}
	
	x = random.choice(list(cards.items()))

	print(x[0])

	return(x)