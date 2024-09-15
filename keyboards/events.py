from aiogram import types


async def get_coworking_keyboard(coworking_info) -> types.ReplyKeyboardMarkup:
    coworking_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                   keyboard=[
                                                       [
                                                           types.KeyboardButton(
                                                               text=f'{coworking["external_id"]}.{coworking["name"]}')
                                                       ]
                                                       for coworking in coworking_info
                                                   ],
                                                   one_time_keyboard=True)

    return coworking_keyboard
