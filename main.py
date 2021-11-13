from aiogram.utils import executor
from create_bot import dp
from handlers import admin, client

async def online(_):
    print('Бот запущен.')

client.register_handlers_client(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=online)