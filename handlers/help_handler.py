from telebot import TeleBot, types

from helper import DATA


def handle(bot: TeleBot):
    @bot.message_handler(commands=['help'])
    def help_handler(message: types.Message):
        if message.chat.type != 'private':
            return

        bot.send_message(
            chat_id=message.from_user.id,
            text=DATA['messages']['help']
        )
