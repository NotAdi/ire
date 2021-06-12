from pyrogram import Client, filters
import requests
import json
import re
import random
#app= Client("my_account")
@Client.on_message(filters.text & ~filters.forwarded & filters.me & filters.command("aniquote","-"))
def quotes(client, message):
    char_name= message.command[1]
    #link=f"https://animechan.vercel.app/api/qoutes/charactername={char_name}"
    chara={"name":char_name}
    quote= requests.get('https://animechan.vercel.app/api/quotes/character', params=chara)
    print(quote.status_code)
    text= quote.json() #json.dumps(quote.json(), sort_keys=True, indent=3)
    #message.edit_text(text)
    #max_val= len(text)
    #quote_number= random.randint(1,max_val)
    #message.edit_text(f"Anime: {text[quote_number]['anime']}\nCharacter: {text[quote_number]['character']}\nQuote: \"{text[quote_number]['quote']}\"")
    final_text= random.choice(text)
    message.edit_text(f"Anime: {final_text['anime']}\n\nCharacter: {final_text['character']}\n\nQuote: \"{final_text['quote']}\"")

#app.run()
