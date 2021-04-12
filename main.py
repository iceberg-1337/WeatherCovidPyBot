import telebot
import pyowm

from pyowm.utils.config import get_default_config

from wearher import get_weather

from telebot import types

from covid import get_covid

bot = telebot.TeleBot('1655397111:AAGOqLwVAicRXDlvic8nYvJ9gSPhBgDV1xc')     #token

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('4d21785a4841673ea7889b3d412f2681', config_dict)
mgr = owm.weather_manager()

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    item1 = types.KeyboardButton('☁ Узнать погоду ☀')
    item2 = types.KeyboardButton('🦠 Узнать про Covid-19 🦠')

    markup.add(item1, item2)

    sti = open('static/AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id,
    "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом. \n что желаете сделать".format(
    message.from_user, bot.get_me()),
    parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, action)


def action(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Во всём мире')
    btn2 = types.KeyboardButton('Украина')
    btn3 = types.KeyboardButton('Россия')
    btn4 = types.KeyboardButton('Беларусь')
    markup.add(btn1, btn2, btn3, btn4)

    if message.chat.type == 'private':
        if message.text == '☁ Узнать погоду ☀':
            bot.send_message(message.from_user.id, 'в каком городе')
            bot.register_next_step_handler(message, get_weather)
        elif message.text == '🦠 Узнать про Covid-19 🦠':
            send_message = f'Чтобы узнать данные напишите страну\n или выберите страну из списка'
            bot.send_message(message.from_user.id, send_message, parse_mode='html', reply_markup=markup)
            bot.register_next_step_handler(message, get_covid)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

# RUN
bot.polling(none_stop=True)