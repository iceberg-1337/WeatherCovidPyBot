import pyowm
from pyowm.utils.config import get_default_config
import telebot

bot = telebot.TeleBot('1655397111:AAGOqLwVAicRXDlvic8nYvJ9gSPhBgDV1xc')

def get_weather(message):
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = pyowm.OWM('4d21785a4841673ea7889b3d412f2681', config_dict)
    mgr = owm.weather_manager()

    obsrevation = mgr.weather_at_place(message.text)
    w = obsrevation.weather
    temp = w.temperature('celsius')["temp"]

    answer = 'В городе ' + message.text + ' сейчас ' + w.detailed_status + '\n'
    answer += 'Температура в районе ' + str(temp) + '\n'

    bot.send_message(message.chat.id, answer)
