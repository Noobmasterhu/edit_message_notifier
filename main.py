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

@edit_bot.on_message(filters.group)
def forward_message(_, m: Message):
    group_id = int(os.environ["group_id"])
    f = m.forward(group_id)
    #link = f.link
    #print("\nmessage:",m.text,"\nmessage link:",link,"\nby:", m.from_user.first_name)


edit_bot.run()
