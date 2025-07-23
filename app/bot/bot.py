import asyncio
from app.bot.logs.logger import logger
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from app.bot.handlers.commands import commands_router
from config.config import settings


async def main():
    logger.info("<=== | Starting bot |===>")

    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(
            parse_mode=ParseMode(settings.bot.parse_mode)
        ),
    )
    dp = Dispatcher()
    dp.include_router(commands_router)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.exception(e)
    finally:
        logger.info("<=== | Turning off bot |===>")
