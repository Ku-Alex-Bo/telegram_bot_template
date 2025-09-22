from aiogram import Router, html
from aiogram.filters import Command
from aiogram.types import Message
from fluentogram import TranslatorRunner

commands_router = Router()

@commands_router.message(Command("start"))
async def start_cmd(
    message: Message,
    i18n: TranslatorRunner,
):
    username = html.quote(message.from_user.full_name)
    await message.answer(
        text=i18n.welcome.text(username=username)
    )

@commands_router.message(Command("help"))
async def help_cmd(
    message: Message,
    i18n: TranslatorRunner,
)
    await message.answer(text=i18n.help.text)


