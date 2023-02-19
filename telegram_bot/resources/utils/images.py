from aiogram.types import Message

from telegram_bot.config.constant_strings import IMAGE_DOWNLOAD_COMPLETED
from telegram_bot.config.env_vars import IMAGE_DOWNLOAD_PATH


class Images:
    @staticmethod
    async def store_image(message: Message):
        await message.photo[-1].download(destination_file=IMAGE_DOWNLOAD_PATH + message.html_text + '.jpg')
        await message.reply(text=IMAGE_DOWNLOAD_COMPLETED)

