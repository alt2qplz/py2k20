'''
Быки и коровы

Компьютер загадывает число из 4 НЕПОВТОРЯЮЩИХСЯ цифр, задача игрока отгадать его,
за меньшее число попыток.

Игра принимает на вход число от игрока и говорит сколько в нем КОРОВ и сколько
БЫКОВ. Корова это цифра, которая есть в числе, но стоит не на своём месте. Бык
это цифра котоаря стоит на своем месие.

ПРИМЕР:

Загаданное число: 3245

Число игрока: 1234

КОРОВЫ: 2
БЫКИ: 1
'''

from generator import get_number

guessed_number = list(get_number())

my_number = ''

korovi = 0
biki = 0
attempt = 0

while my_number != guessed_number:
	my_number = list(input('Введите ЧЕТЫРЕ НЕПОВТОРЯЮЩИЕСЯ цифры: '))

	if len(my_number) != 4:
		print('Введите ЧЕТЫРЕ цифры!\n')
		continue
	for i in range(4):
		if my_number[i] == guessed_number[i]:
			biki += 1
		elif my_number[i] in guessed_number:
			korovi += 1
		else:
			pass

	print(f'\nБЫКИ: {biki}')
	print(f'КОРОВЫ: {korovi}\n')

	biki = 0
	korovi = 0
	attempt += 1

else:
	print(guessed_number)
	print(my_number)
	print(f'ЧИСЛО ПОПЫТОК: {attempt}')
	print('Победа')




