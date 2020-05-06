from pyrogram import Client, Filters
from pyrogram.api import functions
import datetime
import time
import pytz
api_id =  721128 #my.telegram.org dan olgan apiidni qoying
api_hash = "83bb993972326f27ad4e4ef939606e0a" #my.telegram.org dan olgan apihash ni qoying
app = Client("my_account",api_id,api_hash)
app.start()
while True:
    ok = pytz.timezone("Asia/Tashkent")
    x = datetime.datetime.now(tz=ok)
    x = x.strftime("%H:%M")
    app.send(functions.account.UpdateProfile(
    first_name="Rajabov Behruz "+str(x),
    about="O'zbekistonda soat: " +str(x)
    ))
    time.sleep(30)
