from pyrogram import Client
from pyrogram import filters
#with Client("my_account") as app:
 # app.send_message("me", "test")
#app= Client("my_account")
#app.start()
#app.send_message("me", "test")
#app.stop()
#app= Client("my_account")
@Client.on_message(~filters.forwarded & ~filters.sticker & ~filters.via_bot & ~filters.edited & filters.me & filters.command("alive",'-'))
def my_handler(client, message):
    message.edit_text("OwO I am alive")
#app.run()
