from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from New_life_3.config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

if __name__ == '__main__':
    from New_life_3.handler import dp
    executor.start_polling(dp, skip_updates=True)
