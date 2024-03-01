import discord
from discord.ext import commands

import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready():
    print("The bot is ready for use")
    
@client.command()
async def hello(ctx):
    await ctx.send("Hello!")

client.run(os.getenv("TOKEN"))
