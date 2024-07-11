from aiogram_dialog.widgets.kbd import Button, Column, Group, Select
from aiogram_dialog.widgets.text import Const, Format


def product_categories(on_click):
    return Group(
        Select(
            Format('{item[0]}'),
            id='s_categories',
            item_id_getter=lambda x: x[1],
            items='categories',
            on_click=on_click,
        ),
        id='categories',
        width=1
    )


def product_sizes(on_click):
    return Group(
        Select(
            Format('{item}'),
            id='s_sizes',
            item_id_getter=lambda x: x,
            items='sizes',
            on_click=on_click,
        ),
        id='sizes',
        width=1
    )


def product_amounts(on_click):
    return Group(
        Select(
            Format('{item}'),
            id='s_amounts',
            item_id_getter=lambda x: x,
            items='amounts',
            on_click=on_click,
        ),
        id='amounts',
        width=2
    )


def product_colors(on_click):
    return Group(
        Select(
            Format('{item}'),
            id='s_colors',
            item_id_getter=lambda x: x,
            items='colors',
            on_click=on_click,
        ),
        id='colors',
        width=2
    )
