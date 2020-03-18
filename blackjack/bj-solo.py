# Импортируем функцию из другого файла, которая возвращает случайную карту
import random_card


def stats():
	# Вывод текущей статистики
	print('\nКарты у тебя на руках:')
	print(my_cards)
	print('\nСумма очков:')
	print(str(sum) + '\n')

# Созадем пустой список для хранения карт и переменную для подсчета суммы очков
my_cards = []
sum = 0


# Добавляем две карты, название идёт в список, а значение суммируется к sum
for my_card in range(2):
	my_card = random_card.random_card() # Присваеваем my_card кортеж из возвращенных значений
	my_cards.append(my_card[0]) # Первая часть кортежа (название) в список
	sum += int(my_card[1]) # Вторая часть кортежа (значение) в sum

# Выводим статистику
stats()


if sum == 21: # Проверка на выйгрышь
	print('BLACK JACK!')
else:
	print('Ещё карту? (да / нет)\n') # Предлагаем ещё карту
	while str(input()).lower() == 'да': # Если ответить 'да' - запускает добавление карты, аналогичное началу игры
		print()
		my_card = random_card.random_card()
		my_cards.append(my_card[0])
		sum += int(my_card[1])

		# Выводим статистику
		stats()

		if sum == 21: # Проверка на выйгрышь
			print('BLACK JACK!')
			break
		elif sum > 21: # Проверка на проигрышь
			print('Ты проиграл')
			break
		print('Ещё карту?\n')	
	else: # При недоборе и отказе взять карту - выводим счет
		print('\nТвой счет: ' + str(sum))