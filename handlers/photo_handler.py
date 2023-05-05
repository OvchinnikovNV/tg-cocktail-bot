from telebot import TeleBot, types
from os import getenv

from helper import DATA, STATE, get_cocktail_name


def handle(bot: TeleBot):
    @bot.message_handler(content_types=['photo'])
    def photo_handler(message: types.Message):
        if message.chat.type != 'private':
            return

        photo_id = message.photo[-1].file_id
        if photo_id is None:
            return

        user: types.User = message.from_user

        if user.id not in STATE:
            return

        cocktail_name: str = get_cocktail_name(STATE[user.id].cocktail)

        markup = types.InlineKeyboardMarkup()
        btn_accept = types.InlineKeyboardButton(
            text='Принять',
            callback_data=f"accept:{user.id}"
        )
        btn_refuse = types.InlineKeyboardButton(
            text='Отказать',
            callback_data=f"refuse:{user.id}"
        )
        btn_ready = types.InlineKeyboardButton(
            text='Готово',
            callback_data=f"ready:{user.id}"
        )
        markup.add(btn_accept, btn_refuse)
        markup.add(btn_ready)

        bot.send_photo(
            chat_id=getenv('TO_CHAT_ID'),
            photo=photo_id,
            caption=f"{user.first_name} {user.last_name} (https://t.me/{user.username})\n\n"
                    f"Заказ: {cocktail_name}",
            parse_mode="Markdown",
            reply_markup=markup
        )
