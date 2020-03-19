'''
7.9. Без пастрами: используя список sandwich_orders из упражнения 7.8, проследите за
тем, чтобы значение 'pastrami' встречалось в списке как минимум три раза.
Добавьте в начало программы код для вывода сообщения о том, что пастрами больше нет, и напишите
цикл while для удаления всех вхождений 'pastrami' из sandwich_orders. Убедитесь в том,
что в finished_sandwiches значение 'pastrami' не встречается ни одного раза
'''

sandwich_orders = [
	'sandwich classic',
	'pastrami',
	'sandwich modern',
	'pastrami',
	'sandwich postmodern',
	'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
	

while sandwich_orders:
	print(f'I made {sandwich_orders[0]}')
	finished_sandwiches.append(sandwich_orders[0])
	sandwich_orders.remove(sandwich_orders[0])

print('\nЯ приготовил: ', end='')
print(*finished_sandwiches, sep=', ') 