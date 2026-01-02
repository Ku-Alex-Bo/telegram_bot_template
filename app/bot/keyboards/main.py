"""
Main keyboards
"""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Button 1"), KeyboardButton(text="Button 2")],
        [KeyboardButton(text="Button 3"), KeyboardButton(text="Button 4")],
    ],
    resize_keyboard=True,
)