'''
10.12. Сохраненное любимое число: объедините две программы из упражнения 10.11
в один файл. Если число уже сохранено, сообщите его пользователю, а если нет — 
запросите любимое число пользователя и сохраните в файле. Выполните программу дважды,
чтобы убедиться в том, что она работает.
'''

import json

filename = 'number.json'

try:
	with open(filename, 'r') as f:
		number = json.load(f)
	
except FileNotFoundError:
	number = input('Какой твое любимое число? ')
	with open(filename, 'w') as f:
		json.dump(number, f)

else:
	print(f'Я знаю твое любимое число: {number}')