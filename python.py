import discord
import subprocess
import os
from dotenv import load_dotenv


print("Hello World :)")


client = discord.Client()


@client.event
async def on_ready():
    print('I cummed because of {0.user}'.format(client))


@client.event
async def on_message(message): 
    if message.author == client.user:
        return
    if message.content.startswith('!cummed'):
        print("I sent a cum message")
        await message.channel.send('You cummed')
    if message.content.startswith('!gaming'):
        await message.channel.send('yes you are gamingering')
    if message.content.startswith('!minecraft'): #command for batch script
        await message.channel.send('Attempting to start batch script')
        os.system("start cmd /K script.bat")
        
        
client.run(os.getenv('DISCORD_TOKEN'))
