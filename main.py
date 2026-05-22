from pyrogram import Client, filters

API_ID = 27959583
API_HASH = "034e953d9e1cfe6b08cc2b2a76c2011e"
BOT_TOKEN = "8825900558:AAFwkpG7VrrzGAn5gN0ujM8fjofFqjK_5p8"

app = Client(
    "MegaLuffyBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):

    await message.reply_text(
        f"✨ Hello {message.from_user.first_name}\n\n✅ Mega Luffy Musical Bot Is Online!"
    )

@app.on_message(filters.command("ping"))
async def ping(client, message):

    await message.reply_text(
        "🏓 Pong!"
    )

print("✅ Bot Started Successfully")

app.run()
