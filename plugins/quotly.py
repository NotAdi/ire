from pyrogram import Client, filters
import asyncio
import time
from pyrogram.methods.messages import forward_messages
from pyrogram.raw.types.message import Message

@Client.on_message(filters.text & ~filters.forwarded & filters.me & filters.command("quote","-"))
async def quotes(client, message):
    chat_id= message.chat.id
    message_id=message.reply_to_message.message_id
    message_ids=[]
    if(len(message.command)>1):
        for i in range(message_id, message_id+int(message.command[1])):
            message_ids.append(i)
    if(len(message_ids)==0):
        message_ids.append(message_id)
    await client.forward_messages("QuotLyBot", chat_id, message_ids)
    is_sticker=False
    while not is_sticker:
        quote= await quotly_part(client)
        if(quote.sticker):
            await quote.copy(chat_id)
            is_sticker=True
            await quote.delete()
    await asyncio.sleep(2)
    await message.delete()
    #await quote.delete()
    #return host_id
async def quotly_part(client):
    async for quote in client.iter_history("QuotLyBot",limit=1):
        return quote