'''
8.9. Сообщения: создайте список с серией коротких сообщений. Передайте список
функции show_messages(), которая выводит текст каждого сообщения в списке
'''

def show_messages(massages):
	for massage in massages:
		print(massage)

massages = ['Привет', 'Как дела?', 'Что делаешь?']

show_messages(massages)