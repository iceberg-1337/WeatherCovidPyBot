import pyowm
from pyowm.utils.config import get_default_config
import telebot
from telebot import types

bot = telebot.TeleBot('1655397111:AAGOqLwVAicRXDlvic8nYvJ9gSPhBgDV1xc')


def get_weather(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Главное меню", callback_data="back")
    btn2 = types.InlineKeyboardButton("еще раз", callback_data="again_weather")
    markup.add(btn1, btn2)
    try:
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        owm = pyowm.OWM('4d21785a4841673ea7889b3d412f2681', config_dict)
        mgr = owm.weather_manager()

        obsrevation = mgr.weather_at_place(message.text)
        w = obsrevation.weather
        temp = w.temperature('celsius')["temp"]

        answer = 'В городе ' + message.text + ' сейчас ' + w.detailed_status + '\n'
        answer += 'Температура в районе ' + str(temp) + '\n'

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Главное меню", callback_data="back")
        btn2 = types.InlineKeyboardButton("еще раз", callback_data="again_weather")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, answer, reply_markup=markup)
    except Exception as e:
        print(repr(e))
        bot.send_message(message.chat.id, 'я не знаю такого города', parse_mode='html', reply_markup=markup)