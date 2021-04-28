import os,io,discord
from pervTools import *
from dotenv import load_dotenv
import fitbit



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')

authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)


client = discord.Client()

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

    if message.content == '!perv':
        try:
            heart_data = authd_client.intraday_time_series('activities/heart', base_date=get_right_dateFormat(), detail_level='1sec')['activities-heart-intraday']['dataset'][-1]
            BPM = str(heart_data['value'])
            BPM_TEXT = "Jet's heart was last measured beating at " + BPM + " BPM (" + heart_data['time'] + ")"
        except fitbit.exceptions.HTTPTooManyRequests:
            BPM_TEXT = "HEART DATA NOT AVAILABLE (TOO MANY REQUESTS)"
        
        path = takePic()
        picture = discord.File(path)
        await message.channel.send(BPM_TEXT,file=picture)
        os.remove(path)


client.run(TOKEN)

