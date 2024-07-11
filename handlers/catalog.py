from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import Dialog, DialogManager, StartMode
from bson import ObjectId

from config.bot_config import bot
from config.mongo_config import products
from dialogs.for_catalog import windows
from dialogs.for_catalog.states import Catalog

router = Router()
dialog =  Dialog(
    windows.products_types_window(),
    windows.product_size_window(),
    windows.product_amount_window(),
    windows.product_color_window(),
    windows.product_review_window(),
    windows.product_in_cart_window(),
)


@router.message(Command('catalog'))
async def articles_handler(message: Message, dialog_manager: DialogManager):
    await message.delete()
    # Important: always set `mode=StartMode.RESET_STACK` you don't want to stack dialogs
    await dialog_manager.start(Catalog.select_product, mode=StartMode.RESET_STACK)
