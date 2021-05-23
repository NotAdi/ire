from pyrogram import Client, filters, emoji
from pyrogram.types import ChatPermissions
from time import time
import re
import asyncio
import sys
unmute_perm= ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_stickers=True,
    can_send_games=True,
    can_use_inline_bots=True,
    can_add_web_page_previews=True,
    can_send_polls=True,
    can_change_info=True,
    can_invite_users=True,
    can_pin_messages=True,
    can_send_animations=True,
)
def time_compare(mute_list):
    mute_time=-1
    if(mute_list[2]=='s'):
        mute_time= int(mute_list[1])
    elif(mute_list[2]=='m'):
        mute_time= int(mute_list[1])*60
    elif(mute_list[2]=='h'):
        mute_time= int(mute_list[1])*60*60
    elif(mute_list[2]=='d'):
        mute_time= int(mute_list[1])*60*60*24
    return mute_time
#app= Client("my_account")
@Client.on_message(filters.text & ~filters.forwarded & filters.me & filters.command("mute","-"))
async def mute(client, message):
    chat_id= message.chat.id
    user_id= message.reply_to_message.from_user.id
    my_status= await client.get_chat_member(chat_id, "me")
    mem_status= await client.get_chat_member(chat_id, user_id)
    if(mem_status.status=="creator" or mem_status.status=="administrator"):
        await message.edit_text("You can not mute admin/owner")
        await asyncio.sleep(2)
        await message.delete()
        return
    can_mute=False
    if(my_status.status=="creator"):
        can_mute=True
    elif(my_status.status=="administrator"):
        if(my_status.can_restrict_members==True):
            can_mute=True
    mute_time=-1
    if(can_mute==True):
        if(len(message.command)>1):
            temp= (message.command[1])
            mute_list= re.split('(\d+)',temp)
            mute_time= time_compare(mute_list)
            await client.restrict_chat_member(chat_id, user_id, ChatPermissions(), int(time()+mute_time))
            await message.edit_text(f"User Muted for {temp}")
            await asyncio.sleep(2)
            await message.delete()
        elif(mute_time==-1):
            await client.restrict_chat_member(chat_id, user_id, ChatPermissions())
            await message.edit_text("User has been muted indefinitely")
            await asyncio.sleep(2)
            await message.delete()
    else:
        await message.edit_text("Not enough rights to mute")
        await asyncio.sleep(2)
        await message.delete()
@Client.on_message(filters.text & ~filters.forwarded & filters.me & filters.command("unmute","-"))
async def unmute(client, message):
    chat_id= message.chat.id
    user_id= message.reply_to_message.from_user.id
    await client.restrict_chat_member(chat_id, user_id, unmute_perm)
    await message.edit_text("User unmuted!")
    await asyncio.sleep(2)
    await message.delete()
#app.run()

    
