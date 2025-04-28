from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_i18n import I18nContext

admin_commands_router = Router(name=__name__)


@admin_commands_router.message(Command("panel", "admin"))
async def admin_start(message: Message, i18n: I18nContext) -> Message:
    mention = message.from_user.mention_html()
    return await message.answer(text=i18n.get("admin", mention=mention))
