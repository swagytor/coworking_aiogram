import json

import requests

import config


async def check_coworking_auth(auth_data) -> tuple[str, bool]:
    response = requests.post(f"{config.BACKEND_URL}/users/check_coworking_auth/", json=auth_data)

    parsed_response = json.loads(response.json()["detail"])["MESSAGE"]

    if response.status_code == 200:
        return parsed_response, True

    return parsed_response, False


async def create_user(data):
    response = requests.post(f"{config.BACKEND_URL}/users/register_user/", json=data)

    if response.status_code == 200:
        return response, True

    return response, False
