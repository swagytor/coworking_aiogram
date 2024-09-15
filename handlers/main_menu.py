from aiogram import types
from aiogram.fsm.context import FSMContext

from handlers.registration import coworking_auth
from keyboards.main_menu import main_menu_keyboard
from states.main_menu import MainMenuState


async def main_menu(message: types.Message, state: FSMContext):
    await message.reply("Ты в главном меню!", reply_markup=main_menu_keyboard)
    await state.set_state(MainMenuState.main_menu)


async def change_auth_data(message: types.Message, state: FSMContext):
    return await coworking_auth(message, state)
