import datetime as dt

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_dialog import DialogManager

from config.bot_config import bot
from config.mongo_config import products
from config.telegram_config import ADMIN_TELEGRAM_ID
from dialogs.for_catalog.states import Catalog


async def on_main_menu(callback, widget, manager: DialogManager):
    await manager.switch_to(Catalog.select_product)


async def on_select_product(callback, widget, manager: DialogManager, category_id):
    context = manager.current_context()
    context.dialog_data.update(category_id=str(category_id))
    await manager.switch_to(Catalog.select_size)


async def on_select_size(callback, widget, manager: DialogManager, size):
    context = manager.current_context()
    context.dialog_data.update(size=size)
    await manager.switch_to(Catalog.select_amount)


async def on_select_amount(callback, widget, manager: DialogManager, amount):
    context = manager.current_context()
    context.dialog_data.update(amount=amount)
    await manager.switch_to(Catalog.select_color)


async def on_select_color(callback, widget, manager: DialogManager, color):
    context = manager.current_context()
    context.dialog_data.update(color=color)
    await manager.switch_to(Catalog.product_review)


async def on_product_in_cart(callback, widget, manager: DialogManager):
    await manager.switch_to(Catalog.product_in_cart)
