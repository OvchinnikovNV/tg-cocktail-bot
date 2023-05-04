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
            # TODO: сообщить бармену состояние гостя (GuestState) и очистить его
            return

        user: types.User = message.from_user
        cocktail_name: str = get_cocktail_name(STATE[user.id].cocktail)

        bot.send_photo(
            chat_id=getenv('TO_CHAT_ID'),
            photo=photo_id,
            caption=f"{user.first_name} {user.last_name} ({user.username})\n\n"
                    f"Заказ: {cocktail_name}",
            parse_mode="Markdown"
        )

        bot.send_message(
            chat_id=user.id,
            text=DATA['messages']['ordered'].format(cocktail_name),
            parse_mode="Markdown"
        )

        STATE[user.id].clear()
