from pyrogram import Client, filters
import asyncio
import time
from pyrogram.methods.messages import forward_messages
from pyrogram.raw.types.message import Message

host_id=0
@Client.on_message(filters.text & ~filters.forwarded & filters.me & filters.command("quote","-"))
async def quotes(client, message):
    global host_id
    host_id= message.chat.id
    message_id=message.reply_to_message.message_id
    message_ids=[]
    if(len(message.command)>1):
        for i in range(message_id, message_id+int(message.command[1])):
            message_ids.append(i)
    if(len(message_ids)==0):
        message_ids.append(message_id)
    await client.forward_messages("QuotLyBot", host_id, message_ids)
    await asyncio.sleep(2)
    await message.delete()
    #return host_id
@Client.on_message(filters.bot & filters.incoming & filters.sticker)
async def quotly_part(client, message):
    #chat_id= quotes(client, message)
    #global host_id
    await message.copy(host_id)
    await message.delete()
    await asyncio.sleep(10)
    #global host_id
host_id=0