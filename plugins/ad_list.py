from pyrogram import Client, filters, emoji
from pyrogram.types import ChatPermissions
from time import time
import re
import asyncio
import sys

@Client.on_message(filters.text & ~filters.forwarded & filters.me & filters.command("adlist","-"))
async def adminlist(client,message):
    chat_id=message.command[1]
    admin_list=[]
    async for member in client.iter_chat_members(chat_id, filter="administrators"):
        admin_list.append(member.user.id)
    await message.edit_text(admin_list)