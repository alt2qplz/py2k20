'''
10.3. Гость: напишите программу, которая запрашивает у пользователя его имя. Введенный
ответ сохраняется в файле с именем guest.txt.
'''

name = str(input())

with open('guest.txt', 'w') as guest:
	guest.write(name)