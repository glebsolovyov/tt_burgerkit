import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import config
from googlesheets import get_sheet_values
import handlers
bot = Bot(token=config.TELEGRAM_API_KEY)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message=types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=f'Привет, {message.from_user.username}\n'
                                f'Это бот для тестового задания компании БургерКит')


async def __on_startup(_):
    handlers.register_test_complete_handlers(dp)
    asyncio.create_task(handlers.scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=__on_startup)
