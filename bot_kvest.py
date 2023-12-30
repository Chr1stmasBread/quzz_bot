from telebot import *
from info_quzz import *
from time import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Привет! Я бот-квест. Введи /start_quzz чтобы начать играть!\n'
                                           'Памятка\n'
	                                       'Весь текст указанный в *...* счиается вашими мыслями')


@bot.message_handler(commands=['start_quzz'])
def start_quzz(message):
	bot.send_message(message.chat.id, text=Step_1)
	img_path = "E:\\a shotgun.jpg"
	with open(img_path, 'rb') as f:
		bot.send_photo(message.chat.id, f)
	sleep(1)
	bot.send_message(message.chat.id, text=Step_1_1)
	shot_gun = "E:\\12b8c510-b124-4c8c-a312-b78aa2ed4a26_full.jpg"
	mech_gun = "E:\\93f6daa1-3941-47ea-be0a-588609f2c234_full.jpg"
	axe = "E:\\4a1ad3b8-41df-4b01-b7ec-59498e8e48f7_full.jpg"
	with open(axe, 'rb') as f:
		bot.send_photo(message.chat.id, f)
	with open(shot_gun, 'rb') as f:
		bot.send_photo(message.chat.id, f)
	with open(mech_gun, 'rb') as f:
		bot.send_photo(message.chat.id, f)
	sleep(3)
	bot.send_message(message.chat.id, text=Step_1_2)
	sleep(5)
	bot.send_message(message.chat.id, text=Step_1_3)


@bot.message_handler(func=lambda message: True)
def step_1(message):
	answer = message.text
	if answer == '1':
		bot.send_message(message.chat.id, text=Step_1_3_1)
	
	elif answer == '2':
		bot.send_message(message.chat.id, text=Step_1_3_2)
	
	elif answer == '3':
		bot.send_message(message.chat.id, text=Step_1_3_3)
	
	else:
		bot.send_message(message.chat.id, 'Ответ должен быть числом(1, 2, 3)')
	bot.send_message(message.chat.id, text=Step_1_4_1)
	sleep(10)
	bot.send_message(message.chat.id, text=Step_1_4_2)
	bot.send_message(message.chat.id, text=Step_2)
	answer = None
	return answer


@bot.message_handler(func=lambda message: True)
def step_2(message):
	answer = message.text
	if answer == '1':
		bot.send_message(message.chat.id, text=Step_2_1)
	elif answer == '2':
		bot.send_message(message.chat.id, text=Step_2_2)
		answer_1 = message.text
		if answer_1 == "1":
			bot.send_message(message.chat.id, text=Step_2_2_1)
		elif answer_1 == "2":
			bot.send_message(message.chat.id, text=Step_2_2_2)
		elif answer_1 == "3":
			bot.send_message(message.chat.id, text=Step_2_2_3)
		else:
			bot.send_message(message.chat.id, 'Ответ должен быть числом(1, 2, 3)')
	
	elif answer == '3':
		bot.send_message(message.chat.id, text=Step_2_3)
	
	else:
		bot.send_message(message.chat.id, 'Ответ должен быть числом(1, 2, 3)')

bot.polling()
