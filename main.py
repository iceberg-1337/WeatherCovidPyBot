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