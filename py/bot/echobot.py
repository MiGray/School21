import telebot

bot = telebot.TeleBot("1060520234:AAETGrNGZ9ntNNPDsVMUopaeq56RRIt78Qo")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.send_message(message.chat.id, message.text)

bot.polling(none_stop = True)
