from aiogram import Router
from aiogram.filters.exception import ExceptionTypeFilter
from aiogram.types import ErrorEvent
from aiogram_i18n.context import I18nContext
from loguru import logger
from sqlalchemy.exc import SQLAlchemyError

orm_errors_router = Router(name=__name__)


@orm_errors_router.error(ExceptionTypeFilter(SQLAlchemyError))
async def handle_orm_errors(event: ErrorEvent, i18n: I18nContext) -> None:
    update = event.update

    if update.message:
        await update.message.answer(text=i18n.get("error"))

    elif update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.message.answer(text=i18n.get("error"))

    logger.error(f"ORM Error: {event.exception}")
