from aiogram.fsm.state import State, StatesGroup


class RegisterState(StatesGroup):
    registration = State()
    coworking_auth = State()
    enter_email = State()
    enter_password = State()
