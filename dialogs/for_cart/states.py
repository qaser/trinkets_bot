from aiogram.filters.state import State, StatesGroup


class Cart(StatesGroup):
    show_positions = State()
    # order_confirm = State()
