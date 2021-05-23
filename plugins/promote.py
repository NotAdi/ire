from pyrogram import Client, filters, emoji
from pyrogram.types import ChatPermissions
from time import time
import re
import asyncio
import sys

#app= Client("my_account")
async def check_promote(client, message):
    can_promote= False
    chat_id= message.chat.id
    my_status= await client.get_chat_member(chat_id, "me")
    if(my_status.status=="creator"):
        can_promote=True
    elif(my_status.status=="administrator"):
        if(my_status.can_promote_members==True):
            can_promote=True
    if(not can_promote):
        await message.edit_text("Not enough rights to promote")
        await asyncio.sleep(2)
        await message.delete()
    return can_promote
    
@Client.on_message(filters.reply & filters.text & ~filters.forwarded & filters.me & filters.command("promote","-"))
async def promote_rep(client, message):
    chat_id= message.chat.id
    user_id= message.reply_to_message.from_user.id
    mem_status= await client.get_chat_member(chat_id, user_id)
    if(mem_status.status=="creator" or mem_status.status=="administrator"):
        await message.edit_text("Why would you try to promote an admin or the chat owner?")
        await asyncio.sleep(2)
        await message.delete()
        return
    can_promote= await check_promote(client, message)
    if(can_promote):
        if(len(message.command)>1):
            await client.promote_chat_member(chat_id, user_id, is_anonymous=False,
            can_change_info=False,
            can_delete_messages=True,
    		can_restrict_members=True,
    		can_invite_users=True,
    		can_pin_messages=True,
    		can_promote_members=False,
    		can_manage_voice_chats=True)
            await client.set_administrator_title(chat_id, user_id, message.command[1])
            await message.edit_text("Promoted succesfully!")
            await asyncio.sleep(3)
            await message.delete()
        else:
            await client.promote_chat_member(chat_id, user_id, is_anonymous=False,
            can_change_info=False,
            can_delete_messages=True,
    		can_restrict_members=True,
    		can_invite_users=True,
    		can_pin_messages=True,
    		can_promote_members=False,
    		can_manage_voice_chats=True)
            await message.edit_text("Promoted succesfully!")
            await asyncio.sleep(3)
            await message.delete()
    else:
        return

@Client.on_message(~filters.reply & filters.text & ~filters.forwarded & filters.me & filters.command("promote","-"))
async def promote(client, message):
    chat_id= message.chat.id
    #user_id=0
    #user_id= message.reply_to_message.from_user.id
    my_status= await client.get_chat_member(chat_id, "me")
    #mem_status= await app.get_chat_member(chat_id, user_id)
    #if(len(message.command)>1):
    user_id= message.command[1]
    #elif(len(message.command)==1):
       # user_id= message.reply_to_message.from_user.id
    mem_status= await client.get_chat_member(chat_id, user_id)
    if(mem_status.status=="creator" or mem_status.status=="administrator"):
        await message.edit_text("Why would you try to promote an admin or the chat owner?")
        await asyncio.sleep(2)
        await message.delete()
        return
    can_promote=False
    if(my_status.status=="creator"):
        can_promote=True
    elif(my_status.status=="administrator"):
        if(my_status.can_promote_members==True):
            can_promote=True
    #mute_time=-1
    if(can_promote==True):
        if(len(message.command)<3):
            await client.promote_chat_member(chat_id, user_id, is_anonymous=False,
            can_change_info=False,
            can_delete_messages=True,
    		can_restrict_members=True,
    		can_invite_users=True,
    		can_pin_messages=True,
    		can_promote_members=False,
    		can_manage_voice_chats=True)
            await message.edit_text("Promoted succesfully!")
            await asyncio.sleep(3)
            await message.delete()
        else:
            await client.promote_chat_member(chat_id, user_id, is_anonymous=False,
            can_change_info=False,
            can_delete_messages=True,
    		can_restrict_members=True,
    		can_invite_users=True,
    		can_pin_messages=True,
    		can_promote_members=False,
    		can_manage_voice_chats=True)
            await client.set_administrator_title(chat_id, user_id, message.command[2])
            await message.edit_text("Promoted succesfully!")
            await asyncio.sleep(3)
            await message.delete()
    else:
        await message.edit_text("Not enough rights to promote")
        await asyncio.sleep(2)
        await message.delete()
    
