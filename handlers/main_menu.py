from aiogram import types


async def main_menu(message: types.Message):
    await message.reply("Ты в главном меню!", reply_markup=types.ReplyKeyboardRemove())
