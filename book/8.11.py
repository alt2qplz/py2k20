'''
8.11. Архивированные сообщения: начните с программы из упражнения 8.10. Вызовите
функцию send_messages() для копии списка сообщений. После вызова функции выведите
оба списка и убедитесь в том, что в исходном списке остались все сообщения.
'''

massages = ['Привет', 'Как дела?', 'Что делаешь?']
sent_messages = []

def show_messages(massages):
	while massages:
		massage = massages.pop(0)
		print(massage)
		sent_messages.append(massage)
		


#отправляем копию списка
show_messages(massages[:])


print(sent_messages)

#оригинал списка не пострадал
print(massages)