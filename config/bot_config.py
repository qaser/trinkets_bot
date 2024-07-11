from aiogram import Bot, Dispatcher

from config.redis_config import storage
from config.telegram_config import TELEGRAM_TOKEN
from aiogram.client.default import DefaultBotProperties

bot = Bot(
    token=TELEGRAM_TOKEN,
    default=DefaultBotProperties(parse_mode='HTML', protect_content=True)
)
dp = Dispatcher(storage=storage)
