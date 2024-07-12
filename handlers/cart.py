from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import Dialog, DialogManager, StartMode
from bson import ObjectId

from config.bot_config import bot
from config.mongo_config import products
from dialogs.for_cart import windows
from dialogs.for_cart.states import Cart

router = Router()
dialog =  Dialog(
    windows.main_window(),
)


@router.message(Command('cart'))
async def articles_handler(message: Message, dialog_manager: DialogManager):
    await message.delete()
    # Important: always set `mode=StartMode.RESET_STACK` you don't want to stack dialogs
    await dialog_manager.start(Cart.show_positions, mode=StartMode.RESET_STACK)
