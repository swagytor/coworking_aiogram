import requests
from aiogram import types
from aiogram.fsm.context import FSMContext

import config
from handlers.main_menu import main_menu
from keyboards.registration import register_coworking_keyboard
from services.registration import check_coworking_auth, create_user
from states.registration import RegisterState


async def start(message: types.Message, state: FSMContext):
    response = requests.get(f"{config.BACKEND_URL}/users/check_tg_user/?tg_id={message.from_user.id}")

    if response.status_code == 200:
        if response.json()['is_exist']:
            await state.set_state(RegisterState.registration)
            return await main_menu(message)
        else:
            return await registration(message, state)


async def registration(message: types.Message, state: FSMContext):
    await message.reply(
        f"Привет, {message.from_user.full_name}!\n"
        f"Меня зовут НЕпросто БОТ, я помогу тебе записываться в твой коворкинг без лишней траты времени!\n"
        f"Давай начнём с авторизации в ПРОСТО", reply_markup=register_coworking_keyboard
    )
    await state.set_state(RegisterState.coworking_auth)


async def coworking_auth(message: types.Message, state: FSMContext):
    await message.reply(
        "Отлично! Для того, чтобы авторизоваться в коворкинг ПРОСТО, введи почту, к которой привязан твой аккаунт",
        reply_markup=types.ReplyKeyboardRemove())

    await state.set_state(RegisterState.enter_email)


async def enter_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)

    await message.reply("Теперь введи пароль от ПРОСТО(После ввода сообщение удалится)",
                        reply_markup=types.ReplyKeyboardRemove())

    await state.set_state(RegisterState.enter_password)


async def enter_password(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)

    await message.reply("Проверка авторизации в ПРОСТО", reply_markup=types.ReplyKeyboardRemove())

    data = await state.get_data()

    auth_data = {
        'external_email': data['email'],
        "external_password": data['password']
    }

    response, success = await check_coworking_auth(auth_data)

    if success:
        await message.reply("Авторизация прошла успешно!", reply_markup=types.ReplyKeyboardRemove())
        auth_data["username"] = message.from_user.username
        await create_user(auth_data)

        return await main_menu(message)

    else:
        await message.bot.send_message(message.from_user.id, response.text)
        await message.bot.send_message(message.from_user.id, "Авторизация не удалась!",
                                       reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(None)
        return await coworking_auth(message, state)