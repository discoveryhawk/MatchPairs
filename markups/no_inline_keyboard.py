from aiogram import types

keyboardMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboardMenu.add(types.KeyboardButton('Переглянути мої повідомлення'))
keyboardMenu.add(types.KeyboardButton('Надіслати повідомлення'))
