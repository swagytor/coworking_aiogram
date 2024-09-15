from aiogram.fsm.state import StatesGroup, State


class MainMenuState(StatesGroup):
    main_menu = State()
    change_auth_data = State()
