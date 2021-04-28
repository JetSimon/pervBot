import os,io,discord
from pervTools import *
from dotenv import load_dotenv
import fitbit

USE_FITBIT = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

if USE_FITBIT:    
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
    authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)


client = discord.Client()

def BPM():
    if USE_FITBIT:
        #try to add heart BPM text and if not then forget about it
        try:
            heart_data = authd_client.intraday_time_series('activities/heart', base_date=get_right_dateFormat(), detail_level='1sec')['activities-heart-intraday']['dataset'][-1]
            BPM = str(heart_data['value'])
            BPM_TEXT = BPM + " BPM (" + heart_data['time'] + ")"
            return BPM_TEXT
        except fitbit.exceptions.HTTPTooManyRequests:
            print("HEART DATA NOT AVAILABLE (TOO MANY REQUESTS)")
    return None

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content[:5] == '!perv':

        text = BPM() #defaults to None if not using BPM or error, don't worry
            
        if len(message.content.split(" ", 1)) > 1:
            text = message.content.split(" ",1)[1]

        #creates pic and adds text if exists
        path = takePic(text)
        picture = discord.File(path)
        await message.channel.send(file=picture)
        os.remove(path) #delete pic after so jets computer doesnt crash

    elif message.content[:5] == '!meme':
        if len(message.content.split(" ", 1)) > 1 and ":" in message.content:
            text = message.content.split(" ",1)[1]
            top = text.split(":")[0]
            bottom = text.split(":")[1]
            #creates pic and adds text if exists
            path = makeMeme(top, bottom)
            picture = discord.File(path)
            await message.channel.send(file=picture)
            os.remove(path) #delete pic after so jets computer doesnt crash
        else:
            await message.channel.send("MEME MUST BE IN FORMAT !meme [top]:[bottom]")


client.run(TOKEN)

