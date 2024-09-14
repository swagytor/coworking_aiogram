import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.fsm.storage.redis import RedisStorage
from aiogram import F

import config
from handlers import registration
from states.registration import RegisterState


async def start():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - '
                                                   '(%(filename)s).%(funcName)s:%(lineno)d - %(message)s')
    bot = Bot(token=config.TOKEN)
    storage = RedisStorage.from_url(config.REDIS_URL)

    dp = Dispatcher(storage=storage)

    dp.message.register(registration.start, CommandStart())

    dp.message.register(registration.registration, RegisterState.registration)
    dp.message.register(registration.coworking_auth, F.text == "Авторизоваться")
    dp.message.register(registration.enter_email, RegisterState.enter_email)
    dp.message.register(registration.enter_password, RegisterState.enter_password)

    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
