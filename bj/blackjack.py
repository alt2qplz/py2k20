# Импортируем функцию из другого файла, которая возвращает случайную карту
import random_card


def stats():
	# Вывод текущей статистики
	print('\nКарты у тебя на руках:')
	print(my_cards)
	print('\nСумма очков:')
	print(str(summa) + '\n')

def enemy_stats():
	# Вывод текущей статистики
	print('\nКарты противника:')
	print(enemy_cards)
	print('\nСчет опонента:')
	print(str(enemy_summa))

# Созадем пустой список для хранения карт и переменную для подсчета суммы очков
my_cards = []
summa = 0


# Добавляем две карты, название идёт в список, а значение суммируется к summa
for my_card in range(2):
	my_card = random_card.random_card() # Присваеваем my_card кортеж из возвращенных значений
	my_cards.append(my_card[0]) # Первая часть кортежа (название) в список
	summa += int(my_card[1]) # Вторая часть кортежа (значение) в summa

if summa == 22: # Проверка на 2 ТУЗА
	my_cards.remove('ТУЗ')
	my_cards.append('ТУЗ-ЕДИНИЧКА')
	summa -= 10
# Выводим статистику
stats()


if summa == 21: # Проверка на 21
	print('BLACK JACK!\n')
else:
	print('Ещё карту? (да / нет)\n') # Предлагаем ещё карту
	while str(input()).lower() == 'да': # Если ответить 'да' - запускает добавление карты, аналогичное началу игры
		print()

		my_card = random_card.random_card()
		my_cards.append(my_card[0])
		summa += int(my_card[1])

		if summa == 21: # Проверка на 21
			print('\nBLACK JACK!\n')

			stats()
			break

		elif (summa > 21) and ('ТУЗ' in my_cards): # Проверка на наличие туза при переборе
			
			while (summa > 21) and ('ТУЗ' in my_cards):
				my_cards.remove('ТУЗ')
				my_cards.append('ТУЗ-ЕДИНИЧКА')
				summa -= 10

			if summa > 21:
				print('\nПЕРЕБОР\n')

				stats()
				break
			else:
				

				stats()

				print('Ещё карту?\n')
				continue
			
		elif summa > 21: # Проверка на проигрышь
			print('\nПЕРЕБОР\n')

			stats()
			break
		else:
			

			stats()

			print('Ещё карту?\n')
			continue
	# При недоборе и отказе взять карту - выводим счет
	else:
		print('\nТвой счет: ' + str(summa) + '\n')


# ОПОНЕНТ

print('ХОД ОПОНЕНТА:\n')

enemy_cards = []
enemy_summa = 0

for my_card in range(2):
	my_card = random_card.random_card()
	enemy_cards.append(my_card[0])
	enemy_summa += int(my_card[1])

if enemy_summa == 21: # Проверка на 21
	print('\nENEMY BJ')

if enemy_summa == 22: # Проверка на 2 туза
	enemy_cards.remove('ТУЗ')
	enemy_cards.append('ТУЗ-ЕДИНИЧКА')
	enemy_summa -= 10

while enemy_summa <= 17: # Опонент продолжает брать карты пока сумма очков не достигнет > 17
	my_card = random_card.random_card()
	enemy_cards.append(my_card[0])
	enemy_summa += int(my_card[1])

	if enemy_summa == 21: # Проверка на 21
		print('\nENEMY BJ')
		break

	elif (enemy_summa > 21) and ('ТУЗ' in enemy_cards): # Проверка на наличие туза при переборе
		
		while (enemy_summa > 21) and ('ТУЗ' in enemy_cards):
			enemy_cards.remove('ТУЗ')
			enemy_cards.append('ТУЗ-ЕДИНИЧКА')
			enemy_summa -= 10

		if enemy_summa > 21:
			break
		else:
			continue
		
	elif enemy_summa > 21: # Проверка на проигрышь
		break
	else:
		continue

enemy_stats()


print('\nТвой счет:\n' + str(summa) + '\n')

if enemy_summa <= 21 and summa <= 21:
	if summa > enemy_summa:
		print('ПОБЕДА')
	elif summa == enemy_summa:
		print('НИЧЬЯ')
	elif enemy_summa > summa:
		print('ПРОИГРЫШЬ')
else:
	if summa > 21 and enemy_summa > 21:
		print('НИЧЬЯ')
	elif summa > 21:
		print('ПОРАЖЕНИЕ')
	elif enemy_summa > 21:
		print('ПОБЕДА')