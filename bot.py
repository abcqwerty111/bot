import telebot
import main
from decouple import config

bot = telebot.TeleBot(config("token",default=""))
allowed_ids = [int(config("id1",default="")), int(config("id2",default=""))]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	for i in main.get_main_cats():
		button = telebot.types.KeyboardButton(i)
		markup.add(button)
	if message.chat.id in allowed_ids:
		bot.reply_to(message, "Выбери один из предложенных вариантов или попробуй самостоятельно сделать запрос.", reply_markup=markup)
	else:
		bot.send_message(int(config("id1",default="")), message.chat.id)

@bot.message_handler(content_types=['text'])
def message_reply(message):
	if message.chat.id in allowed_ids:
		if message.text != 'Назад':
			try:
				markup1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
				for i in main.get_children(message.text)[0]:
					button1 = telebot.types.KeyboardButton(i)
					markup1.add(button1)
				answer = main.find_action(message.text)
				button2 = telebot.types.KeyboardButton('Назад')
				markup1.add(button2)
			except:
				answer = 'Нет такой категории'
			try:
				m_id = main.get_children(message.text)[1]
			except:
				m_id = 0
			bot.reply_to(message, answer, reply_markup=markup1)#, parse_mode='HTML')
		if message.text == 'Назад':
			markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
			for i in main.get_main_cats():
				button = telebot.types.KeyboardButton(i)
				markup.add(button)
			bot.reply_to(message, "Выбери один из предложенных вариантов или попробуй самостоятельно сделать запрос.", reply_markup=markup)

bot.infinity_polling()