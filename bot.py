import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6349547714:AAGhnKK1Yv_h6lU6IscmJGhKo-xoCvnp69I")

API_ID = int(os.environ.get("API_ID", "28572833"))

API_HASH = os.environ.get("API_HASH", "f27982dd907796571bfc78844f73eaa2")

STRING = os.environ.get("STRING", "BQAOnoCSRZ0VHwoIKSly5ApJLw_Ll0glHTg3dbTq9gWCmy74FAkfREpEhnC9WzhyNuTdYvgYvONlvrjjs1JThqJSozJnaIb9vO0MBpUxKX0_oaWaAiBW_aQOSY8lX_DjsOJ8j-ju0Ath9oCin6-_YMu6oXwT4oEhfttJt13yFxfgp73dGncxxtYF7ufqKgrW7LxHEVfy_buLGXQrNlvoeb-iHF3urgFrK8KBvmdTuq5sJX2yXA2zxaRDFO8qDthpr0N5Wm4S9AblltnvR3uOJGrE97SUnJiS6wXJOTuiWVnh-AIdNJlv17RDaTXQ_zu1g4ow4b8bW2trE4X8TB7x0pQFAAAAAXxXym8A")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
