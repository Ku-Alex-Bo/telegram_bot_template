"""
Exceptions handlers
"""


from aiogram import Router
from aiogram.filters.exception import ExceptionTypeFilter
from aiogram.types.error_event import ErrorEvent
from fluentogram import TranslatorRunner

error_router = Router(name="errors")


@error_router.error(ExceptionTypeFilter(Exception))
async def unknown_error(event: ErrorEvent, i18n: TranslatorRunner):
    await event.update.message.answer(text=i18n.unknown_error)
