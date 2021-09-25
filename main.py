import os

from pyrogram import Client, filters

from pyrogram.types import Message, User


edit_bot = Client(
    "BotNameHere",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


@edit_bot.on_message(filters.edited)
async def edited(bot,message):
	chatid= message.chat.id	
	await bot.send_message(text=f"{message.from_user.mention} Edited This [Message]({message.link})",chat_id=chatid)
	
edit_bot.run()
