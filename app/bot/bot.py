import asyncio
from app.bot.logs.logger import logger
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties


async def main():
    logger.info("<=== | Starting bot |===>")

    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(
            parse_mode=ParseMode(settings.bot.parse_mode)
        ),
    )
    dp = Dispatcher(storage=storage)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.exception(e)
    finally:
        logger.info("<=== | Turning off bot |===>")
