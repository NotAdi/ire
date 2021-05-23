from pyrogram import Client
from pyrogram import filters
import time
from datetime import datetime
#app= Client("my_account")
@Client.on_message(~filters.forwarded & ~filters.sticker & ~filters.via_bot & ~filters.edited & filters.me & filters.command("ping",'-'))
def ping(client, message):
    #s= datetime.now()
    s=time.time()
    message.edit_text("Pong!")
    elapsed= (time.time()-s)*1000
    #elapsed= (datetime.now()-s).microseconds/1000
    message.edit_text(f"Ping is: \n{elapsed:0.2f} ms")
#app.run()
