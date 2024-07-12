from aiogram_dialog.widgets.kbd import Button, Column, Group, Select, Row
from aiogram_dialog.widgets.text import Const, Format
from . import selected


def nav_menu():
    return Row(
        Button(
            Const('⬅️'),
            id='prev',
            on_click=selected.cart_prev
        ),
        Button(
            Format('{pos_num}/{pos_sum}'),
            id='pager',
        ),
        Button(
            Const('➡️'),
            id='next',
            on_click=selected.cart_next
        ),
        when='nav_is_on'
    )
