import requests

import config


async def check_coworking_auth(auth_data) -> tuple[requests.Response, bool]:
    response = requests.post(f"{config.BACKEND_URL}/users/check_coworking_auth/", json=auth_data)

    if response.status_code == 200:
        return response, True

    return response, False


async def create_user(data):
    response = requests.post(f"{config.BACKEND_URL}/users/create_user/", json=data)

    if response.status_code == 200:
        return response, True

    return response, False
