from pyrogram import Client, filters, emoji
from pyrogram.types import ChatPermissions
from time import time
import re
import asyncio
import sys

async def check_ban(client, message):
    can_ban= False
    chat_id= message.chat.id
    my_status= await client.get_chat_member(chat_id, "me")
    if(my_status.status=="creator"):
        can_ban=True
    elif(my_status.status=="administrator"):
        if(my_status.can_restrict_members==True):
            can_ban=True
    if(not can_ban):
        await message.edit_text("Not enough rights to ban!")
        await asyncio.sleep(2)
        await message.delete()
    return can_ban
@Client.on_message(filters.text & ~filters.forwarded & filters.me & filters.command("ban","-"))
async def ban(client, message):
    chat_id= message.chat.id
    user_id= -1
    if(message.reply_to_message):
        user_id= message.reply_to_message.from_user.id
    elif(len(message.command)>1):
        user_id= message.command[1]
    else:
        await message.edit_text("You need to specify the user to ban")
        await asyncio.sleep(5)
        await message.delete()
        return
    can_ban= await check_ban(client, message)
    if(can_ban):
        await client.kick_chat_member(chat_id, user_id)
        await message.edit_text("Banned succesfully!")
        await asyncio.sleep(5)
        await message.delete()
    else:
        return
@Client.on_message(filters.text & ~filters.forwarded & filters.me & filters.command("unban","-"))
async def unban(client, message):
    chat_id= message.chat.id
    user_id= -1
    if(message.reply_to_message):
        user_id= message.reply_to_message.from_user.id
    elif(len(message.command)>1):
        user_id= message.command[1]
    else:
        await message.edit_text("You need to specify the user to ban")
        await asyncio.sleep(5)
        await message.delete()
        return
    can_unban= await check_ban(client, message)
    if(can_unban):
        await client.unban_chat_member(chat_id, user_id)
        await message.edit_text("Unbanned succesfully!")
        await asyncio.sleep(5)
        await message.delete()
    else:
        return