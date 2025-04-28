from aiogram import Router
from aiogram.exceptions import AiogramError
from aiogram.filters.exception import ExceptionTypeFilter
from aiogram.types import ErrorEvent
from aiogram_i18n.context import I18nContext
from loguru import logger

telegram_errors_router = Router(name=__name__)


@telegram_errors_router.error(ExceptionTypeFilter(AiogramError))
async def handle_bad_request(event: ErrorEvent, i18n: I18nContext) -> None:
    update = event.update

    if update.message:
        await update.message.answer(text=i18n.get("error"))

    elif update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.message.answer(text=i18n.get("error"))

    logger.error(f"Telegram Error: {event.exception}")
