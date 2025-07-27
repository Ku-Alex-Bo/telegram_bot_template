import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from app.bot.handlers.commands import commands_router
from config.config import settings
from fluentogram import TranslatorHub
from app.bot.utils.i18n import create_translator_hub
from app.bot.middlewares.i18n import TranslatorRunnerMiddleware

import logging


logging.basicConfig(
    level=getattr(logging, settings.logs.level.upper(), logging.INFO),
    format=settings.logs.format,
)
logger = logging.getLogger(__name__)

async def main():
    logger.info("<=== | Starting bot |===>")

    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(
            parse_mode=ParseMode(settings.bot.parse_mode)
        ),
    )

    translator_hub: TranslatorHub = create_translator_hub()

    dp = Dispatcher()
    dp.include_router(commands_router)

    dp.update.middleware(TranslatorRunnerMiddleware())
    dp.errors.middleware(TranslatorRunnerMiddleware())
    dp.workflow_data.update(
        translator_hub=translator_hub,
    )

    try:
        await dp.start_polling(
            bot,
            translator_hub=translator_hub,
        )
    except Exception as e:
        logger.exception(e)
    finally:
        logger.info("<=== | Turning off bot |===>")
