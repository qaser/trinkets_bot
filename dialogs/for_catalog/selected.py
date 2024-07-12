import datetime as dt
from bson.objectid import ObjectId

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_dialog import DialogManager, StartMode

from config.bot_config import bot
from config.mongo_config import products, carts
from config.telegram_config import ADMIN_TELEGRAM_ID
from dialogs.for_catalog.states import Catalog
from dialogs.for_cart.states import Cart


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
    context = manager.current_context()
    category_id = context.dialog_data['category_id']
    size = context.dialog_data['size']
    amount = context.dialog_data['amount']
    product = products.find_one({'category': ObjectId(category_id), 'size': size})
    position = {
        'product': product['_id'],
        'amount': int(amount),
        'color': context.dialog_data['color'],
        'datetime': dt.datetime.today(),
        'full_price': product['price'] * int(amount)
    }
    carts.update_one(
        {'user_id': manager.event.from_user.id},
        {'$push': {'positions': position}},
        upsert=True
    )
    await manager.switch_to(Catalog.product_in_cart)


async def on_cart(callback, widget, manager: DialogManager):
    # await manager.done()
    await manager.start(Cart.show_positions, mode=StartMode.RESET_STACK)
