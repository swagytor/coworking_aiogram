from aiogram import types

main_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [types.KeyboardButton(text="Записаться в коворкинг")],
    [types.KeyboardButton(text="Изменить авторизационные данные")]
])
