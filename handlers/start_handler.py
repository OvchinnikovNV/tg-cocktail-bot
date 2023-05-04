from telebot import TeleBot, types

from helper import DATA


def handle(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def start_handler(message: types.Message):
        if message.chat.type != 'private':
            return

        for cocktail in DATA['cocktails']:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(
                text="Заказать",
                callback_data=cocktail['callback']
            ))

            bot.send_photo(
                chat_id=message.from_user.id,
                photo=cocktail['img_url'],
                caption=f"{cocktail['name']}\nСостав: {cocktail['composition']}",
                reply_markup=markup,
                parse_mode="Markdown"
            )
