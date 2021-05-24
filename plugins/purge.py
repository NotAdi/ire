from pyrogram import Client, filters
import time
import asyncio

async def allow_purge(client,message):
    chat_id= message.chat.id
    can_purge=False
    mem_status= await client.get_chat_member(chat_id, "me")
    if(mem_status.status=="creator"):
        can_purge=True
    elif(mem_status.status=="administrator"):
        if(mem_status.can_delete_messages==True):
            can_purge=True
    else:
        await message.edit_text("<code>Not enough rights to purge!</code>")
        await asyncio.sleep(5)
        await message.delete()
    return can_purge
async def fast_purge(client, message):
    target_message= message.message_id
    start_message= message.reply_to_message.message_id
    delete_list=[]
    chat_id= message.chat.id
    for i in range(start_message, target_message):
        delete_list.append(i)
    s= time.time()
    await client.delete_messages(chat_id, delete_list) 
    elapsed= time.time()
    await message.edit_text(f"<code>Purge Complete</code>\nTime taken {(elapsed-s):0.2f}s")
    await asyncio.sleep(3)
    await message.delete()
async def slow_purge(client, message,chat_id):
    delete_list=[]
    async for x in client.iter_history(chat_id):
        if(x.text==message.reply_to_message.text):
            delete_list.append(x.message_id)
            break
        else:
            delete_list.append(x.message_id)
    start=time.time()
    for i in delete_list:
        await client.delete_messages(chat_id, i)
    elapsed=time.time()-start
    await client.send_message(chat_id,f"<code>Slow purge complete!</code>\nTime taken: {elapsed:0.2f}s")
@Client.on_message(~filters.forwarded & ~filters.sticker & ~filters.via_bot & ~filters.edited & filters.me & filters.command("purge",'-'))
async def purge(client, message):
    chat_id= message.chat.id
    if message.chat.type in ("supergroup","channel","group"):
        can_purge=await allow_purge(client, message)
    if message.reply:
        if message.chat.type in ("supergroup","channel"):
            if can_purge:
                await fast_purge(client, message)
            else:
                return
        elif(message.chat.type=="group"):
            if can_purge:
                await slow_purge(client, message,chat_id)
            else:
                return
        else:
            await slow_purge(client, message, chat_id)
    else:
        await message.edit_text("<code>Reply to a message to purge</code>")
        await asyncio.sleep(5)
        await message.delete()
    

    