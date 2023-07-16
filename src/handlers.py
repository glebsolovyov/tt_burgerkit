import time
import asyncio
import aioschedule

from src import main
from src.keyboards import test_keyboard
import time

from aiogram import types, Dispatcher

from src.googlesheets import get_sheet_values


class Timer:
    time = None


async def send_test():
    await main.bot.send_message(chat_id=get_sheet_values()[0], text=f'Тест: {get_sheet_values()[1]}',
                           reply_markup=test_keyboard)
    Timer.time = time.time()


async def scheduler():
    aioschedule.every(1).day.at(get_sheet_values()[3]).do(send_test)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
async def completed(callback_query: types.CallbackQuery):
    if time.time() - Timer.time < int(get_sheet_values()[4]):
        await main.bot.send_message(chat_id=-992437882,
                               text=f'Сотрудник: {get_sheet_values()[0]}\nТест: {get_sheet_values()[1]}\nСтатус: выполнен')
    else:
        await main.bot.send_message(chat_id=-992437882,
                               text=f'Сотрудник {get_sheet_values()[0]}\nТест: {get_sheet_values()[1]}\nСтатус: проигнорирован')

    await callback_query.answer()


async def not_completed(callback_query: types.CallbackQuery):
    if time.time() - Timer.time < int(get_sheet_values()[4]):
        await main.bot.send_message(chat_id=-992437882,
                               text=f'Сотрудник: {get_sheet_values()[0]}\nТест: {get_sheet_values()[1]}\nСтатус: не выполнен')
    else:
        await main.bot.send_message(chat_id=-992437882,
                               text=f'Сотрудник {get_sheet_values()[0]}\nТест: {get_sheet_values()[1]}\nСтатус: проигнорирован')

    await callback_query.answer()


def register_test_complete_handlers(dp: Dispatcher):
    callback_query_handlers = [
        {'callback': completed, 'text': 'completed'},
        {'callback': not_completed, 'text': 'not_completed'}
    ]

    for handler in callback_query_handlers:
        dp.register_callback_query_handler(**handler)
