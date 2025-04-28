from aiogram import Dispatcher

from source.config import settings

from .callback_throttling import CallbackThrottlingMiddleware
from .db import DBMiddleware
from .message_throttling import MessageThrottlingMiddleware
from .reporting import ErrorReportingMiddleware


def setup_middlewares(dp: Dispatcher) -> Dispatcher:
    dp.error.middleware(ErrorReportingMiddleware(settings.tg.admin_ids))
    dp.message.middleware(MessageThrottlingMiddleware())
    dp.callback_query.middleware(CallbackThrottlingMiddleware())
    dp.update.middleware(DBMiddleware(dp["session_pool"]))
    return dp
