from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import platform

# =========================
# CONFIG
# =========================

API_ID = 27959583
API_HASH = "034e953d9e1cfe6b08cc2b2a76c2011e"
BOT_TOKEN = "8825900558:AAFwkpG7VrrzGAn5gN0ujM8fjofFqjK_5p8"

OWNER = "@brutal_luffy"
CHANNEL = "https://t.me/brutal_luffy"
SUPPORT = "https://t.me/brutal_luffybot"

START_TIME = time.time()

# =========================
# BOT CLIENT
# =========================

app = Client(
    "MegaLuffyMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# =========================
# START COMMAND
# =========================

@app.on_message(filters.command("start"))
async def start(client, message):

    uptime = int(time.time() - START_TIME)

    text = f"""
✨ Hey {message.from_user.first_name} 💖

🎵 Welcome To Mega Luffy Musical Bot 🎵

━━━━━━━━━━━━━━━━━━
🔥 Premium Music Bot
⚡ Fastest Downloader
🎬 HD Video Support
🎧 Unlimited Songs
━━━━━━━━━━━━━━━━━━

👨‍💻 Developer : {OWNER}
⚙️ Status : Online ✅
⏰ Uptime : {uptime} sec
💻 System : {platform.system()}

━━━━━━━━━━━━━━━━━━

🌟 Available Commands 🌟

🎵 /song = Download Song
🎬 /video = Download Video
🏓 /ping = Check Speed
📚 /help = Help Menu
👑 /owner = Owner Info
📊 /stats = Bot Stats

━━━━━━━━━━━━━━━━━━

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
                    "📚 Help",
                    callback_data="help"
                ),
                InlineKeyboardButton(
                    "👨‍💻 Owner",
                    callback_data="owner"
                )
            ],
            [
                InlineKeyboardButton(
                    "📢 Updates",
                    url=CHANNEL
                ),
                InlineKeyboardButton(
                    "💬 Support",
                    url=SUPPORT
                )
            ]
        ]
    )

    await message.reply_photo(
        photo="https://graph.org/file/8d5cbbe8c3f7dfc3a7b56.jpg",
        caption=text,
        reply_markup=buttons
    )

# =========================
# PING COMMAND
# =========================

@app.on_message(filters.command("ping"))
async def ping(client, message):

    await message.reply_text(
        "🏓 Pong!\n⚡ Mega Luffy Bot Is Working Perfectly"
    )

# =========================
# HELP COMMAND
# =========================

@app.on_message(filters.command("help"))
async def help_command(client, message):

    help_text = """
📚 Mega Luffy Help Menu

🎵 /song songname
Download Songs

🎬 /video videoname
Download Videos

🏓 /ping
Check Bot Speed

📊 /stats
Check Bot Statistics

👑 /owner
Developer Information
"""

    await message.reply_text(help_text)

# =========================
# OWNER COMMAND
# =========================

@app.on_message(filters.command("owner"))
async def owner(client, message):

    text = f"""
👨‍💻 Owner Information

🔥 Owner : {OWNER}
🎵 Bot : Mega Luffy Musical Bot
⚡ Version : v2.0
🚀 Hosted On Railway

📢 Updates :
{CHANNEL}

💬 Support :
{SUPPORT}
"""

    await message.reply_text(text)

# =========================
# STATS COMMAND
# =========================

@app.on_message(filters.command("stats"))
async def stats(client, message):

    uptime = int(time.time() - START_TIME)

    text = f"""
📊 Mega Luffy Statistics

⚡ Status : Online
⏰ Uptime : {uptime} sec
💻 System : {platform.system()}
🔥 Bot Running Smoothly
"""

    await message.reply_text(text)

# =========================
# SONG COMMAND
# =========================

@app.on_message(filters.command("song"))
async def song(client, message):

    if len(message.command) < 2:

        await message.reply_text(
            "❌ Example:\n/song faded"
        )

        return

    query = " ".join(message.command[1:])

    await message.reply_text(
        f"""
🎵 Song Downloader

🔎 Searching Song :
{query}

⏳ Please Wait...
"""
    )

# =========================
# VIDEO COMMAND
# =========================

@app.on_message(filters.command("video"))
async def video(client, message):

    if len(message.command) < 2:

        await message.reply_text(
            "❌ Example:\n/video alone"
        )

        return

    query = " ".join(message.command[1:])

    await message.reply_text(
        f"""
🎬 Video Downloader

🔎 Searching Video :
{query}

⏳ Please Wait...
"""
    )

# =========================
# CALLBACK BUTTONS
# =========================

@app.on_callback_query()
async def callbacks(client, callback_query):

    data = callback_query.data

    if data == "music":

        await callback_query.message.edit_caption(
            caption="""
🎵 Music Downloader

Use Like :

/song faded
"""
        )

    elif data == "video":

        await callback_query.message.edit_caption(
            caption="""
🎬 Video Downloader

Use Like :

/video alone
"""
        )

    elif data == "help":

        await callback_query.message.edit_caption(
            caption="""
📚 Help Commands

/start
/help
/ping
/song
/video
/stats
/owner
"""
        )

    elif data == "owner":

        await callback_query.message.edit_caption(
            caption=f"""
👨‍💻 Owner

🔥 {OWNER}
⚡ Mega Luffy Musical Bot
🚀 Powered By Pyrogram
"""
        )

# =========================
# BOT START
# =========================

print("✅ Mega Luffy Musical Bot Started Successfully")

app.run()
