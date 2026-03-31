import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ButtonStyle


BOT_TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="▶️ Watch Now",
                    callback_data="watch",
                    style=ButtonStyle.PRIMARY,
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ Premium",
                    callback_data="premium",
                    style=ButtonStyle.SUCCESS,
                )
            ],
            [
                InlineKeyboardButton(
                    text="🗑 Delete",
                    callback_data="delete",
                    style=ButtonStyle.DANGER,
                )
            ],
        ]
    )

    # Invisible text so it looks like only buttons
    await message.answer("\u2063", reply_markup=keyboard)


@dp.callback_query(F.data == "watch")
async def watch_cb(callback):
    await callback.answer("Watch clicked")


@dp.callback_query(F.data == "premium")
async def premium_cb(callback):
    await callback.answer("Premium clicked")


@dp.callback_query(F.data == "delete")
async def delete_cb(callback):
    await callback.message.delete()


async def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing")

    logging.basicConfig(level=logging.INFO)
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
