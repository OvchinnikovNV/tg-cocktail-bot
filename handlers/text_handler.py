from telebot import TeleBot, types

from helper import DATA


def handle(bot: TeleBot):
    @bot.message_handler(content_types=['text'])
    def text_handler(message: types.Message):
        if message.chat.type != 'private':
            return

        bot.send_message(
            message.from_user.id,
            message.text
        )
