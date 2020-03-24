'''
Бот для телеграма который играет в БК
Проблема в том, что не получается отдель сгенерировать число поэтому пока только
в ручном режиме
'''

import telebot

from telebot import types

import config

from generator import get_number

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def bk(message):
	'''играем в Быки и Коровы'''

	guessed_number = list('0157')

	korovi = 0
	biki = 0

	my_number = list(message.text)

	# bot.send_message(message.chat.id, f'ЧИСЛО: {guessed_number}')
	if message.text == 'test':
		bot.send_message(message.chat.id, f'ЧИСЛО: {guessed_number}')
	if len(my_number) != 4:
		bot.send_message(message.chat.id,'Введите ЧЕТЫРЕ цифры!\n')
	elif my_number == guessed_number:
		bot.send_message(message.chat.id, f'\nБЫКИ: 4')	
		bot.send_message(message.chat.id, 'ПОБЕДА')

		korovi = 0
		biki = 0

		
	else:
		for i in range(4):
			if my_number[i] == guessed_number[i]:
				biki += 1
			elif my_number[i] in guessed_number:
				korovi += 1
			else:
				pass

		bot.send_message(message.chat.id, f'\nБЫКИ: {biki}\nКОРОВЫ: {korovi}\n')
		biki = 0
		korovi = 0


bot.polling(none_stop=True)