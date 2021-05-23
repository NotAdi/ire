from pyrogram import Client, filters, emoji
#app= Client("my_account")
@Client.on_message(~filters.forwarded & ~filters.sticker & ~filters.edited & ~filters.via_bot & filters.mentioned)
def mention_alert(client, message):
    chat_id= message.chat.id
    chat_name= message.chat.title
    message_id=message.message_id
    message_link= message.link
    text= f"The message was sent in {emoji.SPARKLE} {chat_name} \n\nThe link to the message is {message_link}"
    #list_possible=True
    #if(message_id!=1 & message_id)
    client.send_message(-378435915,text, disable_web_page_preview=True)
    client.forward_messages(-378435915,chat_id, message_id)
#app.run()
