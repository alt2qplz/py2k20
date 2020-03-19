a = int(input())

if a % 4 == 0:
	if (a % 400 == 0):
		print('Високосный')
	elif (a % 100 == 0):
		print('Обычный')
	else:
		print('Високосный')
else:
	print('Обычный')

'''
Все тут будет коммент
'''

