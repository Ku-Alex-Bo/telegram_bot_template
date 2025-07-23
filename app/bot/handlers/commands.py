from aiogram import Bot, Router
from aiogram.filters import Command, CommandStart

commands_router = Router()

@commands_router.message(CommandStart())
async def start_command(message):
    await message.answer("Welcome! Use /help to see available commands.")


