from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from fluentogram import TranslatorRunner

commands_router = Router()


@commands_router.message(Command("start"))
async def start_cmd(
    message: Message,
    i18n: TranslatorRunner,
):
    user = message.from_user
    if user is None:
        return

    username = user.full_name

    if username:
        text = i18n.welcome.text(username=username)
    else:
        text = i18n.welcome.text.stranger

    await message.answer(text=text)


@commands_router.message(Command("help"))
async def help_cmd(
    message: Message,
    i18n: TranslatorRunner,
):
    await message.answer(text=i18n.help.text())
