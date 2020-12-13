import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online)
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = '야나어 사전'))

    print('봇 이름 :', client.user.name, ',', '봇 아이디 :', client.user.id, '봇 버전 :', discord.__version__)

client.run(os.environ['Nzg3NjQzNjg0NDA1NTEwMTc0.X9X8WA.v5aK2_JS343VatRISvDdXFf1NyY'])