'''
9.13. Кубики: создайте класс Die с одним атрибутом sides, который имеет значение по
умолчанию 6. Напишите метод roll_die() для вывода случайного числа от 1 до количества
граней на кубике. Создайте экземпляр, представляющий 6-гранный кубик, и смоделируйте
10 бросков.
Создайте экземпляры, представляющие 10- и 20-гранный кубик. Смоделируйте 10 бросков
каждого кубика
'''

from random import randint

class Die():
	'''Игральный кубик'''

	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		print(randint(1,self.sides))

standart_die = Die()

standart_die.roll_die()

die_10 = Die(10)
die_20 = Die(20)

die_10.roll_die()

die_20.roll_die()