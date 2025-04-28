from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram_i18n.types import KeyboardButton, ReplyKeyboardMarkup

reply_language_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Русский"), KeyboardButton(text="English")],
    ],
    resize_keyboard=True,
)
