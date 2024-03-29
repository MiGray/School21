import telebot
from telebot import types

TOKEN = '1060520234:AAETGrNGZ9ntNNPDsVMUopaeq56RRIt78Qo'
bot = telebot.TeleBot(TOKEN)	

name = ''
surname = ''
age = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "What is your name?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Write /reg')

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'What is your surname?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id,'How old are you?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Numbers, please')
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    key_yes = types.InlineKeyboardButton(text = 'Yes', callback_data = 'yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text = 'No', callback_data = 'no')
    keyboard.add(key_no)
    question = ('Your ' + str(age) + ' years, you called ' + name + ' ' + surname + '?')
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Save : )')
    elif call.data == "no":
        bot.register_next_step_handler(message, get_name)

bot.polling(none_stop = True, interval=0)
