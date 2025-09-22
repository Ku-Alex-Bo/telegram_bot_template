from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner

commands_router = Router()

@commands_router.message(CommandStart())
async def start_command(
    message: Message,
    i18n: TranslatorRunner,
):
    username = html.quote(message.from_user.full_name)
    await message.answer(
        text=i18n.welcome.text(username=username)
    )


