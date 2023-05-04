from telebot import TeleBot, types

from helper import DATA, STATE, GuestState, get_cocktail_name


def handle(bot: TeleBot):
    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call: types.CallbackQuery):
        user_id: int = call.from_user.id

        if user_id not in STATE:
            STATE[user_id] = GuestState(
                username=call.from_user.username,
                first_name=call.from_user.first_name,
                last_name=call.from_user.last_name
            )

        STATE[user_id].cocktail = call.data

        bot.send_message(
            chat_id=user_id,
            text=DATA['messages']['selfie'].format(get_cocktail_name(call.data)),
            parse_mode="Markdown"
        )
