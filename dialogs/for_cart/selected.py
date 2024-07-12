import datetime as dt
from bson.objectid import ObjectId

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_dialog import DialogManager, StartMode

from config.bot_config import bot
from config.mongo_config import products, carts
from config.telegram_config import ADMIN_TELEGRAM_ID
from dialogs.for_cart.states import Cart
from dialogs.for_catalog.states import Catalog


async def on_main_menu(callback, widget, manager: DialogManager):
    await manager.switch_to(Cart.show_positions)


async def cart_next(callback, widget, manager: DialogManager):
    context = manager.current_context()
    saved_pos = int(context.dialog_data['pos_num'])
    pos_sum = int(context.dialog_data['pos_sum']) - 1
    new_pos = saved_pos + 1 if saved_pos < pos_sum else 0
    context.dialog_data.update(pos_num=new_pos)
    await manager.switch_to(Cart.show_positions)


async def cart_prev(callback, widget, manager: DialogManager):
    context = manager.current_context()
    saved_pos = int(context.dialog_data['pos_num'])
    pos_sum = int(context.dialog_data['pos_sum']) - 1
    new_pos = saved_pos - 1 if saved_pos > 0 else pos_sum
    context.dialog_data.update(pos_num=new_pos)
    await manager.switch_to(Cart.show_positions)


async def delete_position(callback, widget, manager: DialogManager):
    context = manager.current_context()
    pos_num = int(context.dialog_data['pos_num'])
    user_id = manager.event.from_user.id
    user_cart = carts.find_one({'user_id': user_id})
    positions = user_cart.get('positions')
    positions.pop(pos_num)
    carts.update_one(
        {'user_id': user_id},
        {'$set': {'positions': positions}}
    )
    context.dialog_data.update(pos_num=0)
    await manager.switch_to(Cart.show_positions)


async def on_catalog(callback, widget, manager: DialogManager):
    # await manager.done()
    await manager.start(Catalog.select_product, mode=StartMode.RESET_STACK)
