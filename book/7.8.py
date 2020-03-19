'''
7.8. Сэндвичи: создайте список с именем sandwich_orders, заполните его названиями 
различных видов сэндвичей. Создайте пустой список с именем finished_sandwiches. 
В цикле переберите элементы первого списка и выведите сообщение для каждого 
элемента (например, «I made your tuna sandwich»). После этого каждый сэндвич из 
первого списка перемещается в список finished_sandwiches. После того как все 
элементы первого списка будут обработаны, выведите сообщение с перечислением всех 
изготовленных сэндвичей.
'''

sandwich_orders = ['sandwich classic', 'sandwich modern', 'sandwich postmodern']
finished_sandwiches = []

while sandwich_orders:
	print(f'I made {sandwich_orders[0]}')
	finished_sandwiches.append(sandwich_orders[0])
	sandwich_orders.remove(sandwich_orders[0])

print('\nЯ приготовил: ', end='')
print(*finished_sandwiches, sep=', ') 