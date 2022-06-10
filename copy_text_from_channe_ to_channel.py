"""

--------------------------------------------------------------
Robot copying channel text to another channel.

(C) 2022 Saeed Mirzamohammadi, Qazvin, Iran

Email: saeed1843mirzamohammadi@gmail.com

2022/6/9
--------------------------------------------------------------


"""

from colorama import Fore,init
from pyrogram import Client
from pyrogram import filters
import pyromod.listen


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bot=Client("cli_bot",
api_id=12345678,                                 #api id Account  
api_hash="00fd81e939a89v3335259fh0693c2l8")      #api hash Account
senderـchannel="abcd"                            #Sender Channel ID                
receiver_channel="abcd"                          #Receiver channel ID
admin_id=1234567890                              #id bot Admin
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ____________________________________________________________________________________________________
init()
print(Fore.YELLOW+"● Bot is online ●")
@bot.on_message(filters.channel)
async def send_text(client ,message):
    if message.chat.username == senderـchannel:     
        async for post in bot.get_chat_history(senderـchannel,limit=1):  
            await bot.send_message(receiver_channel,post.text)          #send to channel
#____________________________________________________________________________________________________

#--------------------------------------------------------------------------------------------------------
@bot.on_message(filters.user(admin_id)&filters.command("/start",'')&filters.private)  #Online bot test
async def test_on_bot(client,message):
    try:
        await bot.send_message(admin_id, "Bot is online")
    except:
        pass
#--------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    bot.run()