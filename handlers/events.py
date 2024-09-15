import requests
from aiogram import types
from aiogram.fsm.context import FSMContext

import config
from handlers.main_menu import main_menu
from keyboards.events import get_coworking_keyboard
from services.events import get_qr_code
from states.events import EventState


async def register_to_coworking(message: types.Message, state: FSMContext):
    coworking_info = requests.get(f"{config.BACKEND_URL}/coworkings/").json()
    coworking_keyboad = await get_coworking_keyboard(coworking_info)

    await message.reply("В какой коворкинг вы хотите записаться?", reply_markup=coworking_keyboad)

    await state.set_state(EventState.choose_coworking)


async def choose_coworking(message: types.Message, state: FSMContext):
    external_id = message.text.split(".")[0]

    data = {
        "coworking_id": external_id,
        "tg_id": message.from_user.id
    }

    response = requests.post(f"{config.BACKEND_URL}/events/register_user_event/", json=data)

    if response.status_code == 200:
        response = response.json()
        await message.bot.send_message(message.from_user.id,
                                       response['detail'],
                                       reply_markup=types.ReplyKeyboardRemove())

        qr = await get_qr_code(response['qr_code'])
        await message.bot.send_photo(message.from_user.id, qr)

    else:
        await message.reply("Произошла ошибка при записи в коворкинг")

        await state.set_state(None)

    return await main_menu(message, state)
