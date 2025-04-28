from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_language_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Русский", callback_data="language_ru")],
        [InlineKeyboardButton(text="English", callback_data="language_en")],
    ],
)
