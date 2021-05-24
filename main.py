import telebot
from telebot import types
from wearher import get_weather
from covid import get_covid

bot = telebot.TeleBot('1655397111:AAGOqLwVAicRXDlvic8nYvJ9gSPhBgDV1xc')  # token


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton('☁ Узнать погоду ☀', callback_data='weather')
    item2 = types.InlineKeyboardButton('🦠 Узнать про Covid-19 🦠', callback_data='corona')

    markup.add(item1, item2)

    sti = open('static/AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть "
                     "подопытным кроликом. \n что желаете сделать".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    def covid():
        markup1 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn2 = types.KeyboardButton('Украина')
        btn3 = types.KeyboardButton('Россия')
        btn4 = types.KeyboardButton('Беларусь')
        markup1.add(btn2).add(btn3).add(btn4)

        send_message = f'Чтобы узнать данные напишите страну\n или выберите страну из списка'
        message1 = bot.send_message(call.from_user.id, send_message, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(message1, get_covid)

    def weather():
        message = bot.send_message(call.from_user.id, 'В каком городе?')
        bot.register_next_step_handler(message, get_weather)

    if call.data == 'weather':
        weather()

    elif call.data == 'corona':
        covid()

    elif call.data == 'back':
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text="☁ Узнать погоду ☀", callback_data="weather")
        item2 = types.InlineKeyboardButton(text="🦠 Узнать про Covid-19 🦠", callback_data="corona")
        markup.add(item1, item2)
        bot.send_message(call.message.chat.id, 'что желаете сделать?', reply_markup=markup)

    elif call.data == 'again_weather':
        weather()

    elif call.data == 'again_covid':
        covid()

    else:
        bot.send_message(call.message.chat.id, 'Я не знаю что ответить 😢')


@bot.message_handler(content_types='text')
def send_echo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Главное меню", callback_data="back")
    markup.add(btn1)
    bot.send_message(message.chat.id, "напиши /start\nили нажми на кнопку", reply_markup=markup)


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling(none_stop=True)
