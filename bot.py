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
