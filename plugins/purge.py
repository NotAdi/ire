from pyrogram import Client, filters, emoji
import time
import asyncio
#api_id=1570429
#api_hash="8b9bb59393b50ec875f63cef8529012b"
#app= Client("my_account")

@Client.on_message(~filters.forwarded & ~filters.sticker & ~filters.via_bot & ~filters.edited & filters.me & filters.command("purge",'-'))
async def purge(client, message):
    target_message= message.message_id
    start_message= message.reply_to_message.message_id
    delete_list=[]
    chat_id= message.chat.id
    can_purge=False
    mem_status= await client.get_chat_member(chat_id, "me")
    if(mem_status.status=="creator"):
        can_purge=True
    elif(mem_status.status=="administrator"):
        if(mem_status.can_delete_messages==True):
            can_purge=True
    if(can_purge==True):
        for i in range(start_message, target_message):
            delete_list.append(i)
        s= time.time()
        await client.delete_messages(chat_id, delete_list) 
        elapsed= time.time()
        await message.edit_text(f"Purge Complete {emoji.CHECK_MARK_BUTTON}\nTime taken {(elapsed-s):0.2f}s")
        await asyncio.sleep(3)
        await message.delete()
    else:
        await message.edit_text("Not enough rights to delete messages!")
        await asyncio.sleep(3)
        await message.delete()
#Client.run()
