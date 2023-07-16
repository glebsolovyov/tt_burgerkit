from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_completed = InlineKeyboardButton(text='Выполнено', callback_data='completed')
button_not_completed = InlineKeyboardButton(text='Не выполнено', callback_data='not_completed')

test_keyboard = InlineKeyboardMarkup(row_width=1).add(button_completed, button_not_completed)