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

@client.command(aliases = ['h','help'])
async def Help(ctx):
    embed = discord.Embed(title = Help, description = "Enter >Helpxtal to get help for Xtal Commands\nEnter >Helpremainder to get help for Remainder Commands\nEnter >Helplvl to get get help for Lvling command", color = discord.Colour.red())
    await ctx.send(embed=embed)

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
    
    @client.command(aliases = ['MinRemainder','minremainder','Minremainder','MinuteRemainder','minuteremainder'])
    async def Minuteremainder(ctx, time: int,*,msg):
        while True:
            await s(60*time)
            embed = discord.Embed(title = Minuteremainder, description = f"{msg},{ctx.author.mention}", color = discord.Colour.red())
            await ctx.send(embed=embed)
def lvl():
    @client.command(aliases = ['helplvl','HelpLvl'])
    async def Helplvl(ctx):
        embed = discord.Embed(title = Helplvl, description = "Command for just put >lvl(lvl you wanna search for)", color = discord.Colour.red())
        await ctx.send(embed=embed)

    @client.command(aliases = ['leveling','lvl','Lvl'])
    async def Leveling(ctx,lv):
        PATH = "chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get("https://coryn.club")
        print(driver.title)
        lv=lv
        search = driver.find_element_by_name("lv")
        search.send_keys(lv)
        search.send_keys(Keys.RETURN)

        try:
            l = []
            aa = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[1]")))
            a = aa.text
            bb = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[2]")))
            b = bb.text
            cc = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[3]")))
            c = cc.text
            dd = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[4]")))
            d = dd.text
            l.append(a)
            l.append(b)
            l.append(c)
            l.append(d)
            listToStr = ' \n\n '.join([str(elem) for elem in l])  
            
            embed = discord.Embed(description = "" , color = discord.Colour.red())
            embed.add_field(name = f"Bosse's for {Leveling} at Lvl {lv} are:",value = listToStr)
            await ctx.send(embed=embed)

        finally:
            driver.quit() 

            
lvl()            
rem()
