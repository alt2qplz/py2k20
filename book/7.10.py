'''
7.10. Отпуск мечты: напишите программу, которая опрашивает пользователей, где бы они
хотели провести отпуск. Включите блок кода для вывода результатов опроса.
'''

poll = True
poll_result = {}

while poll:
	name = str(input('Как тебя зовут? '))
	work = str(input('Где ты работаещь? '))

	poll_result[name] = work

	if str(input('Добавить ещё участника? ')) == 'нет':
		poll = False

for name, work in poll_result.items():
	print(f'{name} работает {work}')