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

love_card = ['ТУЗ']

# Выводим ключи

'''
На самом деле перебор ключей используется по умолчанию при переборе словаря,
так что этот код будет работать точно так же, как если бы вы не писали keys()
'''

for i in sorted(cards):
	print(i)

	if i in love_card:
		print('ХАЙ')