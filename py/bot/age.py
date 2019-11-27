import telebot

TOKEN = '1060520234:AAETGrNGZ9ntNNPDsVMUopaeq56RRIt78Qo'
bot = telebot.TeleBot(TOKEN)	

#bot = telebot.TeleBot("1060520234:AAETGrNGZ9ntNNPDsVMUopaeq56RRIt78Qo")

#@bot.message_handler(commands=['start', 'help'])
#def send_welcome(message):
#	bot.reply_to(message, "Howdy, how are you doing?")

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#	bot.reply_to(message, message.text)

name = '';
surname = '';
age = 0;
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "What is your name?");
        bot.register_next_step_handler(message, get_name); 
    else:
        bot.send_message(message.from_user.id, 'Write /reg');

def get_name(message):
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'What is your surname?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id,'How old are you?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    while age == 0: 
        try:
            age = int(message.text) 
        except Exception:
            bot.send_message(message.from_user.id, 'Numbers, please');
    bot.send_message(message.from_user.id, 'You ' + str(age) + ' year, your called ' + name + ' ' + surname + '?')

bot.polling(none_stop = True)