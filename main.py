from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import platform

API_ID = 27959583
API_HASH = "034e953d9e1cfe6b08cc2b2a76c2011e"
BOT_TOKEN = "8825900558:AAFwkpG7VrrzGAn5gN0ujM8fjofFqjK_5p8"

OWNER_USERNAME = "@brutal_luffy"
UPDATES_CHANNEL = "https://t.me/brutal_luffy"
SUPPORT_GROUP = "https://t.me/brutal_luffybot"

START_TIME = time.time()

app = Client(
    "LuffyyMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):

    uptime = int(time.time() - START_TIME)

    text = f"""
✨ Hello {message.from_user.first_name} 💖

🎵 Welcome To Luffyy Musical Bot 🎵

━━━━━━━━━━━━━━━━━━
🔥 Premium Music Bot
⚡ Fastest Downloader
🎬 HD Video Support
🎧 Unlimited Songs
━━━━━━━━━━━━━━━━━━

👨‍💻 Developer : {OWNER_USERNAME}
⚙️ Status : Online ✅
⏰ Uptime : {uptime} sec

━━━━━━━━━━━━━━━━━━

🎵 /song = Download Song
🎬 /video = Download Video
🏓 /ping = Check Speed
📚 /help = Help Menu

💖 Enjoy Your Music Journey
"""

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🎵 Music",
                    callback_data="music"
                ),
                InlineKeyboardButton(
                    "🎬 Video",
                    callback_data="video"
                )
            ],
            [
                InlineKeyboardButton(
                    "📢 Updates",
                    url=UPDATES_CHANNEL
                ),
                InlineKeyboardButton(
                    "💬 Support",
                    url=SUPPORT_GROUP
                )
            ]
        ]
    )
