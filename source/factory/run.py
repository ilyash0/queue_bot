# run.py
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from loguru import logger

from source.config import settings


async def run_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    logger.info("Starting polling...")
    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dispatcher.start_polling(
            bot,
            allowed_updates=dispatcher.resolve_used_update_types(),
        )
    finally:
        logger.info("Polling stopped.")


async def run_webhook(dispatcher: Dispatcher, bot: Bot) -> None:
    logger.info("Starting webhook...")

    webhook_url = f"{settings.webhook.url.rstrip('/')}{settings.webhook.path}"
    secret = settings.webhook.secret
    await bot.set_webhook(
        url=webhook_url,
        secret_token=secret,
        allowed_updates=dispatcher.resolve_used_update_types(),
        drop_pending_updates=True,
    )

    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dispatcher,
        bot=bot,
        secret_token=settings.webhook.secret,
    )
    webhook_requests_handler.register(app, path=settings.webhook.path)
    setup_application(app, dispatcher, bot=bot)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host=settings.webhook.host, port=settings.webhook.port)
    logger.info(
        f"Starting aiohttp server on {settings.webhook.host}:{settings.webhook.port}",
    )
    await site.start()

    await asyncio.Event().wait()

    await runner.cleanup()
    await bot.delete_webhook()
