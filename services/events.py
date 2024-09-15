import base64

from aiogram import types


async def get_qr_code(qr_data):
    # Удаляем префикс data:image/png;base64,
    qr_data = qr_data.split(",")[1]

    # Декодируем строку Base64
    image_data = base64.b64decode(qr_data)

    # Создаем изображение
    image = types.BufferedInputFile(file=image_data, filename="qr.png")

    # Возвращаем InputFile
    return image
