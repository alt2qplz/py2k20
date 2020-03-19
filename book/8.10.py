'''
8.10. Отправка сообщений: начните с копии вашей программы из упражнения 8.9. 
Напишите функцию send_messages(), которая выводит каждое сообщение и перемещает его
в новый список с именем sent_messages. После вызова функции выведите оба списка 
и убедитесь в том, что перемещение прошло успешно.
'''


massages = ['Привет', 'Как дела?', 'Что делаешь?']
sent_messages = []

def show_messages(massages):
	while massages:
		massage = massages.pop(0)
		print(massage)
		sent_messages.append(massage)
		



show_messages(massages)

print(sent_messages)
print(massages)