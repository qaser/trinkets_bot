from aiogram.filters.state import State, StatesGroup


class Catalog(StatesGroup):
    select_product = State()
    select_size = State()
    select_amount = State()
    select_color = State()
    product_review = State()
    product_in_cart = State()
