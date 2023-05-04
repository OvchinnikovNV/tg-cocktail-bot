from os import getenv
from telebot import TeleBot
from dotenv import load_dotenv

from handlers import start_handler, help_handler, text_handler, photo_handler, callback_handler


load_dotenv()

bot = TeleBot(token=getenv('TG_TOKEN'))

start_handler.handle(bot)
help_handler.handle(bot)
text_handler.handle(bot)
photo_handler.handle(bot)
callback_handler.handle(bot)
