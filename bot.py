from asyncio.tasks import sleep, wait, wait_for
import discord
import asyncio
from discord import channel
from discord import emoji
from discord.ext import commands
from asyncio import sleep as s
from discord.ext.commands.core import guild_only
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


client = commands.Bot(command_prefix = ">")
client.remove_command ('help')

@client.event
async def on_ready():
    print("Bot is ready")
def rem():
    @client.command(asliases = ['helpremainder','HelpRemainder'])
    async def Helpremainder(ctx):
        embed = discord.Embed(title = Helpremainder, description = "There are 2 types of Remainder:\n\n1.Remainder Which is an Hour remainder\nCommand for it is Remainder (Time in Hours) (Message that you want to get printed)\n\n2.Minuteremainder Which is an Minute remainder\nCommand for it is Minuteremainder (Time in Minutes) (Message that you want to get printed)\nIf you still face any problem report it on our discord server https://discord.gg/g8DjAvSM", color = discord.Colour.red())
        await ctx.send(embed=embed)


    @client.command(aliases = ['HourRemainder','hourremainder','remainder','Hourremainder'])
    async def Remainder(ctx, time: int,*,msg):
        while True:
            await s(600*time)
            embed = discord.Embed(title = Remainder, description = f"{msg},{ctx.author.mention}", color = discord.Colour.red())
            await ctx.send(embed=embed)
rem()
