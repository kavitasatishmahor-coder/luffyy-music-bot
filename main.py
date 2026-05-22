from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

API_ID = 27959583
API_HASH = "034e953d9e1cfe6b08cc2b2a76c2011e"
BOT_TOKEN = "8825900558:AAFwkpG7VrrzGAn5gN0ujM8fjofFqjK_5p8"

OWNER = "@brutal_luffy"

START_TIME = time.time()

app = Client(
    "MegaLuffyBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):

    uptime = int(time.time() - START_TIME)

    text = f"""
✨ Hello {message.from_user.first_name} 💖

🎵 Mega Luffy Musical Bot 🎵

━━━━━━━━━━━━━━
👨‍💻 Owner : {OWNER}
⚡ Status : Online
⏰ Uptime : {uptime} sec
━━━━━━━━━━━━━━

🎵 /song
🎬 /video
📚 /help
🏓 /ping
"""

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🎵 Music", callback_data="music"),
                InlineKeyboardButton("🎬 Video", callback_data="video")
            ],
            [
                InlineKeyboardButton("👨‍💻 Owner", url="https://t.me/brutal_luffy")
            ]
        ]
    )

    await message.reply_text(
        text,
        reply_markup=buttons
    )

@app.on_message(filters.command("ping"))
async def ping(client, message):

    await message.reply_text(
        "🏓 Pong!"
    )

@app.on_message(filters.command("help"))
async def help(client, message):

    await message.reply_text(
        """
📚 Help Menu

/start - Start Bot
/ping - Check Bot
/help - Help Menu
/song - Download Song
/video - Download Video
"""
    )

@app.on_message(filters.command("song"))
async def song(client, message):

    await message.reply_text(
        "🎵 Song Downloader Coming Soon..."
    )

@app.on_message(filters.command("video"))
async def video(client, message):

    await message.reply_text(
        "🎬 Video Downloader Coming Soon..."
    )

print("✅ Mega Luffy Bot Started")

app.run()
