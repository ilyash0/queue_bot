from aiogram import Bot
from aiogram.types import (
    BotCommand,
    BotCommandScopeAllPrivateChats,
    BotCommandScopeChat,
)

from source.config import settings


async def set_default_commands(bot: Bot) -> None:
    admins = settings.tg.admin_ids

    common_commands = [
        BotCommand(command="start", description="Launch bot"),
        BotCommand(command="help", description="Instructions for use"),
        BotCommand(command="language", description="Change language"),
    ]

    admin_commands = [
        BotCommand(command="start", description="Launch bot"),
        BotCommand(command="help", description="Instructions for use"),
        BotCommand(command="language", description="Change language"),
        BotCommand(command="admin", description="Admin command"),
    ]

    await bot.set_my_commands(common_commands, scope=BotCommandScopeAllPrivateChats())

    await bot.set_my_commands(common_commands)

    for admin_id in admins:
        await bot.set_my_commands(
            admin_commands, scope=BotCommandScopeChat(chat_id=admin_id),
        )
