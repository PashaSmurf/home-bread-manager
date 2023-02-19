import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import ContentTypes, Message

from telegram_bot.config.constant_strings import \
    DOWNLOAD_LOADING, DOWNLOAD_COMPLETED, MIGRATION_COMPLETED
from telegram_bot.config.env_vars import TELEGRAM_API_TOKEN, EXCEL_DOWNLOAD_PATH
from telegram_bot.resources.excel.migration import Migration
from telegram_bot.resources.utils.images import Images

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)
migration = Migration()
images = Images()


@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def file_handle(message: Message):
    await message.reply(text=DOWNLOAD_LOADING)
    await message.document.download(destination_file=EXCEL_DOWNLOAD_PATH)
    await message.reply(text=DOWNLOAD_COMPLETED)
    migration.excel_migration()
    await message.reply(text=MIGRATION_COMPLETED)


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def image_handle(message: Message):
    await images.store_image(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
