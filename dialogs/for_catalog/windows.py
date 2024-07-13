from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import (Back, Button, Cancel, CurrentPage,
                                        NextPage, PrevPage, Row, Url)
from aiogram_dialog.widgets.text import Const, Format
from aiogram.types import ContentType
from aiogram_dialog.widgets.media import StaticMedia

import utils.constants as texts
from dialogs.for_catalog.states import Catalog

from . import getters, keyboards, selected

CATALOG_HEADER = 'Здесь Вы можете ознакомиться со всеми продуктами и заказать товар!'


async def exit_menu(callback, button, dialog_manager):
    try:
        await dialog_manager.done()
        await callback.message.delete()
    except:
        pass


def products_types_window():
    return Window(
        Const('<b>Каталог</b>\n'),
        Const(CATALOG_HEADER),
        keyboards.product_categories(selected.on_select_product),
        Cancel(Const('🔚 Выход'), on_click=exit_menu),
        state=Catalog.select_product,
        getter=getters.get_product_category
    )


def product_size_window():
    return Window(
        Const('Выберите размер'),
        keyboards.product_sizes(selected.on_select_size),
        Back(Const(texts.BACK_BUTTON)),
        state=Catalog.select_size,
        getter=getters.get_sizes,
    )


def product_amount_window():
    return Window(
        Const('Выберите тираж'),
        keyboards.product_amounts(selected.on_select_amount),
        Back(Const(texts.BACK_BUTTON)),
        state=Catalog.select_amount,
        getter=getters.get_amounts,
    )


def product_color_window():
    return Window(
        Const('Выберите цвет акрила'),
        keyboards.product_colors(selected.on_select_color),
        Back(Const(texts.BACK_BUTTON)),
        state=Catalog.select_color,
        getter=getters.get_colors,
    )


def product_review_window():
    return Window(
        StaticMedia(
            path="static/img/trinket.jpg",
            type=ContentType.PHOTO,
        ),
        Const('<u>Ваш выбор:</u>'),
        Format('<b>Товар:</b> {product}'),
        Format('<b>Размер:</b> {size}'),
        Format('<b>Цвет:</b> {color}'),
        Format('<b>Тираж:</b> {amount} шт.'),
        Format('<b>Цена за единицу:</b> {price} руб.\n'),
        Format('<b>Общая цена:</b> {full_price} руб.'),
        Button(
            Const('✅ Добавить в корзину'),
            id='add_order',
            on_click=selected.on_product_in_cart
        ),
        Back(Const(texts.BACK_BUTTON)),
        state=Catalog.product_review,
        getter=getters.get_product,
    )


def product_in_cart_window():
    return Window(
        Const('Заказ в корзине 🛍️'),
        Const('Вы можете перейти в корзину или выбрать еще товар'),
        Button(
            Const('✨ Выбрать еще товар'),
            id='select_product',
            on_click=selected.on_main_menu
        ),
        Button(
            Format('🛍️ Перейти в корзину ({pos_sum})'),
            id='cart',
            on_click=selected.on_cart
        ),
        Button(
            Const('🔚 Выход'),
            id='exit',
            on_click=exit_menu
        ),
        state=Catalog.product_in_cart,
        getter=getters.get_positions,
    )
