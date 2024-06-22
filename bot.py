import discord
from dotenv import load_dotenv
import json
import os

load_dotenv()

# Load bot token from environment variable
TOKEN = os.getenv('DISCORD_TOKEN')

# Initialize client with intents
intents = discord.Intents.default()
intents.members = True  # Enable the members intent to access member information
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Load JSON data
with open('data.json', 'r') as file:
    data = json.load(file)
    role_name = data['ppl1']

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await channel.send(f'{user.mention} がお助けします')

client.run(TOKEN)
