from aiogram import Dispatcher
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import FluentRuntimeCore

from source.config import settings
from source.database import db_manager
from source.telegram import setup_middlewares, setup_routers


def create_dispatcher() -> Dispatcher:
    storage = RedisStorage(
        redis=settings.redis.redis_connection(),
        key_builder=DefaultKeyBuilder(with_bot_id=True, with_destiny=True),
    )
    dp = Dispatcher(storage=storage, session_pool=db_manager.session_maker)

    setup_middlewares(dp)
    setup_routers(dp)

    i18n_middleware = I18nMiddleware(
        core=FluentRuntimeCore(path="source/locales/{locale}"),
    )
    i18n_middleware.setup(dp)
    return dp
