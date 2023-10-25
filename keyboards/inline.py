from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup


def int_kb(i: int = 5):
    builder = InlineKeyboardBuilder()
    for a in range(0, i):
        builder.add(InlineKeyboardButton(text = str(a), callback_data="int_{}".format(a)))
    return builder.as_markup()