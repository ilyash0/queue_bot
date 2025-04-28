from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram_i18n import I18nContext

from source.services import UserService
from source.telegram.keyboards import inline_keyboard_builder, inline_language_keyboard

user_commands_router = Router(name=__name__)


@user_commands_router.message(CommandStart())
async def start(
    message: Message, i18n: I18nContext, user_service: UserService,
) -> Message:
    user = message.from_user

    await user_service.register_user(
        user.id,
        user.first_name,
        user.username,
        user.language_code,
    )

    register_user = await user_service.get_user(user.id)

    if not register_user:
        await i18n.set_locale(user.language_code or "ru")

    mention = user.mention_html()
    return await message.reply(
        text=i18n.greeting(mention=mention),
        reply_markup=inline_keyboard_builder(
            i18n.get("button"),
            "on_click_data",
            locale=i18n.get_current().locale,
        ),
    )


@user_commands_router.message(Command("help"))
async def help(message: Message, i18n: I18nContext) -> Message:
    return await message.reply(
        text=i18n.get("help"),
    )


@user_commands_router.message(Command("language"))
async def language(message: Message, i18n: I18nContext) -> Message:
    return await message.reply(
        text=i18n.get("change_language"),
        reply_markup=inline_language_keyboard,
    )
