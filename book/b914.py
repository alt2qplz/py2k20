'''
9.14. Лотерея: создайте список или кортеж, содержащий серию из 10 чисел и 5 букв. 
Случайным образом выберите 4 числа или буквы из списка. Выведите сообщение о том, что
билет, содержащий эту комбинацию из четырех цифр или букв, является выигрышным.
'''


from random import choice

ticket = [i for i in range(0, 10)]

for i, elem in enumerate(ticket):
    ticket[i] = str(elem)

ticket.extend(['A', 'B', 'C', 'D', 'E']) #Добавить несколько элементов

def get_ticket():
	return(choice(ticket) + choice(ticket) + choice(ticket) + choice(ticket))



lucky_ticket = get_ticket()

print(lucky_ticket)

