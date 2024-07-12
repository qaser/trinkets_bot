from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import (Back, Button, Cancel, CurrentPage,
                                        NextPage, PrevPage, Row, Url)
from aiogram_dialog.widgets.text import Const, Format, Multi

import utils.constants as texts
from dialogs.for_cart.states import Cart

from . import getters, keyboards, selected

CART_IS_EMPTY = 'Ваша корзина пуста, перейдите в каталог чтобы выбрать товары'
FOOTER_DELETE = 'Чтобы удалить товар нажмите кнопку ❌'
FOOTER_NAV = 'Для навигации по корзине используйте кнопки ⬅️ / ➡️'


async def exit_menu(callback, button, dialog_manager):
    try:
        await dialog_manager.done()
        await callback.message.delete()
    except:
        pass


def main_window():
    return Window(
        Const(CART_IS_EMPTY, when='cart_is_empty'),
        Multi(
            Format('<b>Корзина на сумму {cart_price} руб.</b>'),
            Format('Показан товар {pos_num} из {pos_sum}', when='nav_is_on'),
            Format('\n<b>Наименование:</b> {product}'),
            Format('<b>Размер:</b> {size}'),
            Format('<b>Цвет:</b> {color}'),
            Format('<b>Тираж:</b> {amount} шт.'),
            Format('<b>Цена за единицу:</b> {price} руб.'),
            Format('<b>Цена за тираж:</b> {full_price} руб.\n'),
            # Format('Товар добавлен в корзину {date}г.'),
            Const(FOOTER_DELETE),
            Const(FOOTER_NAV, when='nav_is_on'),
            sep='\n',
            when='cart_not_empty'
        ),
        Button(
            Const('❌ Удалить из заказа'),
            id='cart_delete',
            on_click=selected.delete_position,
            when='cart_not_empty'
        ),
        keyboards.nav_menu(),
        Button(
            Const('✅ Сделать заказ'),
            id='order_accept',
            # on_click=selected.create_order,
            when='cart_not_empty'
        ),
        Button(
            Const('🗂️ Перейти в каталог товаров'),
            id='to_catalog',
            on_click=selected.on_catalog,
            when='cart_is_empty'
        ),
        Cancel(Const('🔚 Выход'), on_click=exit_menu),
        state=Cart.show_positions,
        getter=getters.get_cart_positions
    )
