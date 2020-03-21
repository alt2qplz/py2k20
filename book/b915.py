'''
4D52

9.15. Анализ лотереи: напишите цикл, который проверяет, насколько сложно выиграть
в смоделированной вами лотерее. Создайте список или кортеж с именем my_ticket. 
Напишите цикл, который продолжает генерировать комбинации до тех пор, пока не 
выпадет выигрышная комбинация. Выведите сообщение с информацией о том, сколько выполнений
цикла понадобилось для получения выигрышной комбинации.
'''

from random import choice

def get_ticket():
	return(choice(ticket) + choice(ticket) + choice(ticket) + choice(ticket))

ticket = [i for i in range(0, 10)]
for i, elem in enumerate(ticket):
    ticket[i] = str(elem)
ticket.extend(['A', 'B', 'C', 'D', 'E']) #Добавить несколько элементов




my_ticket = get_ticket()

i = 1

while my_ticket != '9A67':
	my_ticket = get_ticket()
	i += 1



print(my_ticket)
print(i)