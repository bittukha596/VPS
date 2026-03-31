import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "color_buttons_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("▶️ Watch Now", callback_data="watch")],
            [InlineKeyboardButton("✨ Premium", callback_data="premium")],
            [InlineKeyboardButton("🗑 Delete", callback_data="delete")],
        ]
    )

    await message.reply_text(
        "\u2063",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("^watch$"))
async def watch_handler(client, callback_query):
    await callback_query.answer("Watch clicked", show_alert=False)

@app.on_callback_query(filters.regex("^premium$"))
async def premium_handler(client, callback_query):
    await callback_query.answer("Premium clicked", show_alert=False)

@app.on_callback_query(filters.regex("^delete$"))
async def delete_handler(client, callback_query):
    try:
        await callback_query.message.delete()
    except Exception:
        await callback_query.answer("Can't delete this message", show_alert=False)

app.run()
