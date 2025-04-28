import asyncio

from aiogram import Bot, Dispatcher
from loguru import logger

from source.config import settings
from source.database import create_tables, db_manager
from source.factory import create_bot, create_dispatcher, run_polling, run_webhook
from source.utils import set_default_commands, setup_logger


async def on_startup_common(bot: Bot) -> None:
    await create_tables()
    await set_default_commands(bot)


async def on_shutdown_common(bot: Bot) -> None:
    if db_manager:
        await db_manager.dispose()


async def start_bot() -> None:
    setup_logger()
    logger.info("Initializing bot...")

    bot: Bot = create_bot()
    dp: Dispatcher = create_dispatcher()

    dp.startup.register(on_startup_common)
    dp.shutdown.register(on_shutdown_common)

    logger.info(
        f"Starting bot in {'webhook' if settings.webhook.use else 'polling'} mode.",
    )
    try:
        if settings.webhook.use:
            await run_webhook(dispatcher=dp, bot=bot)
        else:
            await run_polling(dispatcher=dp, bot=bot)
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped by user.")
    except Exception as e:
        logger.exception(f"An error occurred during bot execution: {e}")
    finally:
        if bot and bot.session:
            await bot.session.close()
        logger.info("Bot stopped.")


if __name__ == "__main__":
    asyncio.run(start_bot())
