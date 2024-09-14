import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

import config


async def start():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - '
                                                   '(%(filename)s).%(funcName)s:%(lineno)d - %(message)s')
    bot = Bot(token=config.TOKEN)
    storage = RedisStorage.from_url(config.REDIS_URL)

    dp = Dispatcher(storage=storage)

    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
