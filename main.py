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



    bot.send_message(message.chat.id,
    "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом. \n что желаете сделать".format(
    message.from_user, bot.get_me()),
    parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, action)