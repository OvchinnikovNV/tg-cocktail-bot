from telebot import TeleBot, types
from os import getenv

from helper import DATA, STATE, GuestState, get_cocktail_name


def handle(bot: TeleBot):
    def is_barmen_callback(user_id: int) -> bool:
        return user_id == int(getenv('ADMIN_ID'))

    @bot.callback_query_handler(func=lambda call: not is_barmen_callback(call.from_user.id))
    def guest_handler(call: types.CallbackQuery):
        user_id: int = call.from_user.id

        if user_id not in STATE:
            STATE[user_id] = GuestState(
                username=call.from_user.username,
                first_name=call.from_user.first_name,
                last_name=call.from_user.last_name
            )

        if STATE[user_id].is_making:
            bot.send_message(
                chat_id=user_id,
                text=DATA['messages']['selfie'].format(get_cocktail_name(call.data)),
                parse_mode="Markdown"
            )
            return

        STATE[user_id].cocktail = call.data

        bot.send_message(
            chat_id=user_id,
            text=DATA['messages']['selfie'].format(get_cocktail_name(call.data)),
            parse_mode="Markdown"
        )

    @bot.callback_query_handler(func=lambda call: is_barmen_callback(call.from_user.id))
    def barmen_handler(call: types.CallbackQuery):
        action, user_id = call.data.split(':')
        user_id: int = int(user_id)

        if action == 'accept':
            bot.send_message(
                chat_id=user_id,
                text=DATA['messages']['accept'].format(get_cocktail_name(STATE[user_id].cocktail)),
                parse_mode="Markdown"
            )
            STATE[user_id].is_making = True
        elif action == 'refuse':
            bot.send_message(
                chat_id=user_id,
                text=DATA['messages']['refuse'],
                parse_mode="Markdown"
            )
        elif action == 'ready':
            bot.send_message(
                chat_id=user_id,
                text=DATA['messages']['ready'].format(get_cocktail_name(STATE[user_id].cocktail)),
                parse_mode="Markdown"
            )
            STATE[user_id].clear()

