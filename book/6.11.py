'''
6.11. Города: создайте словарь с именем cities. Используйте названия трех городов
в качестве ключей словаря. Создайте словарь с информацией о каждом городе;
включите в него страну, в которой расположен город, примерную численность населения
и один примечательный факт, относящийся к этому городу. Ключи словаря каждого
города должны называться country, population и fact.
Выведите название каждого города и всю сохраненную информацию о нем.
'''

cities = {
	'Kazan': {
		'country' : 'Russia',
		'population' : '1.5 million',
		'fact' : "I'm was born here"
	},

	'Tokyo-3': {
		'country' : 'Japan',
		'population' : 'no information',
		'fact' : 'this is fictional city'
	},

	'New-York' : {
		'country' : 'USA',
		'population' : 'over 8 million',
		'fact' : 'ALL <3 NY'
	}
}

for city, city_d in cities.items():
	print(city)
	for d in city_d.items():
		print(f'{d[0]} : {d[1]}')
	else:
		print()