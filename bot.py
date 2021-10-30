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
    
    @client.command(aliases = ['MiniBoss','miniboss'])
    async def Miniboss(ctx,lv):
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
            aa = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[3]/div[1]")))
            a = aa.text
            bb = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[3]/div[2]")))
            b = bb.text
            cc = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[3]/div[3]")))
            c = cc.text
            dd = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[3]/div[4]")))
            d = dd.text
            l.append(a)
            l.append(b)
            l.append(c)
            l.append(d)
            listToStr = ' \n\n '.join([str(elem) for elem in l])  
            embed = discord.Embed(description = "" , color = discord.Colour.red())
            embed.add_field(name = f"Minibosse's for {Miniboss} lvling at Lvl {lv} are:",value = listToStr)
            await ctx.send(embed=embed)

        finally:
            driver.quit() 

@client.command(asliases = ['helpitem','HelpItem'])
async def Helpitem(ctx):
        embed = discord.Embed(title = Helpitem, description = "underconstruction", color = discord.Colour.red())
        await ctx.send(embed=embed)

@client.command(aliases = ['item'])
async def Item(ctx,*,msg):
    PATH = "chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://coryn.club")
    print(driver.title)
    msg = msg
    search = driver.find_element_by_css_selector("#main-menu > div.all-menu > form:nth-child(7) > input[type=text]")    
    search.send_keys(msg)
    search.send_keys(Keys.RETURN)
    try:
        try:
            aa = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[1]/div[1]")))
            a = aa.text
            bb = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[2]/div[1]")))
            b = bb.text
            cc = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[3]/div[1]")))
            c = cc.text 
            dd = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[4]/div[1]")))
            d = dd.text 
            ee = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[5]/div[1]")))
            e = ee.text 
            shit1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/text()")))
            shit = shit1.text
            # ff = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[6]/div[1]")))
            # f = ff.text 
            # gg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[7]/div[1]")))
            # g = gg.text 
            # hh = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[8]/div[1]")))
            # h = hh.text 
            # ii = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[9]/div[1]")))
            # i = i.text 
            # jj = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[10]/div[1]")))
            # j = jj.text 
            # kk = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[11]/div[1]")))
            # k = kk.text 
            # ll = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[12]/div[1]")))
            # l = ll.text 
            # mm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[13]/div[1]")))
            # m = mm.text


            


        finally:
            if a == a:
                a1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[1]/ul/li[1]/div[2]")))
                a11 = a1.text
                a1a = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/ul/li[2]")
                a1a.click()
                a1111 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[1]/ul/li[2]/div[2]/div[2]")))
                a11111 = a1111.text
                global embeda
                embeda = discord.Embed(color = discord.Colour.red())
                embeda.add_field(name = a,value = a11+"\n\n"+a11111)

                a2a = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/ul/li[1]")
                a2a.click()
                a2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[1]/ul/li[1]/div[2]")))
                a22 = a2.text
                a2a2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/ul/li[2]")
                a2a2.click()
                a222 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[1]/ul/li[2]/div[2]/div[2]")))
                a2222 = a222.text
                global embeda1
                embeda1 = discord.Embed(color = discord.Colour.red())
                embeda1.add_field(name = a,value = a22+"\n\n"+a2222)

            if b == b:
                b1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[2]/ul/li[1]/div[2]")))
                b11 = b1.text
                b1b = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/ul/li[2]")
                b1b.click()
                b1111 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[2]/ul/li[2]/div[2]/div[2]")))
                b11111 = b1111.text
                global embedb
                embedb = discord.Embed(color = discord.Colour.red())
                embedb.add_field(name = b,value = b11+"\n\n"+b11111)

                b2b = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/ul/li[1]")
                b2b.click()
                b2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[2]/ul/li[1]/div[2]")))
                b22 = b2.text
                b2b2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/ul/li[2]")
                b2b2.click()
                b222 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[2]/ul/li[2]/div[2]/div[2]")))
                b2222 = b222.text
                global embedb1
                embedb1 = discord.Embed(color = discord.Colour.red())
                embedb1.add_field(name = b,value = b22+"\n\n"+b2222)
            
            if c == c:
                c1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[3]/ul/li[1]/div[2]")))
                c11 = c1.text
                c1c = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/ul/li[2]")
                c1c.click()
                c1111 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[3]/ul/li[2]/div[2]/div[2]")))
                c11111 = c1111.text
                global embedc
                embedc = discord.Embed(color = discord.Colour.red())
                embedc.add_field(name = c,value = c11+"\n\n"+c11111)

                c2c = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/ul/li[1]")
                c2c.click()
                c2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[3]/ul/li[1]/div[2]")))
                c22 = c2.text
                c2c2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/ul/li[2]")
                c2c2.click()
                c222 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[3]/ul/li[2]/div[2]/div[2]")))
                c2222 = c222.text
                global embedc1
                embedc1 = discord.Embed(color = discord.Colour.red())
                embedc1.add_field(name = c,value = c22+"\n\n"+c2222)
            
            if d == d:
                d1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[4]/ul/li[1]/div[2]")))
                d11 = d1.text
                d1d = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[4]/ul/li[2]")
                d1d.click()
                d1111 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[4]/ul/li[2]/div[2]/div[2]")))
                d11111 = d1111.text
                global embedd
                embedd = discord.Embed(color = discord.Colour.red())
                embedd.add_field(name = d,value = d11+"\n\n"+d11111)

                d2d = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[4]/ul/li[1]")
                d2d.click()
                d2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[4]/ul/li[1]/div[2]")))
                d22 = d2.text
                d2d2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[4]/ul/li[2]")
                d2d2.click()
                d222 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[4]/ul/li[2]/div[2]/div[2]")))
                d2222 = d222.text
                global embedd1
                embedd1 = discord.Embed(color = discord.Colour.red())
                embedd1.add_field(name = d,value = d22+"\n\n"+d2222)
            
            if e == e:
                e1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[5]/ul/li[1]/div[2]")))
                e11 = e1.text
                e1e = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[5]/ul/li[2]")
                e1e.click()
                e1111 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[5]/ul/li[2]/div[2]/div[2]")))
                e11111 = e1111.text
                global embede
                embede = discord.Embed(color = discord.Colour.red())
                embede.add_field(name = e,value = e11+"\n\n"+e11111)

                e2e = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[5]/ul/li[1]")
                e2e.click()
                e2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[5]/ul/li[1]/div[2]")))
                e22 = e2.text
                e2e2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[5]/ul/li[2]")
                e2e2.click()
                e222 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[5]/ul/li[2]/div[2]/div[2]")))
                e2222 = e222.text
                global embede1
                embede1 = discord.Embed(color = discord.Colour.red())
                embede1.add_field(name = e,value = e22+"\n\n"+e2222)
            
            
            if shit == "No result found":
                embed = discord.Embed(description = "No result found", color = discord.Colour.red())
                await ctx.send(embed=embed)
            
            

                
            
            
                #listToStr = "\n\n".join([str(elem) for elem in l])
                #embed = discord.Embed(color = discord.Colour.red())
                #embed.add_field(name = f"Results",value = listToStr)
                #mssg = await ctx.send(embed=embed)
                        
                            
                    
                        
    finally:
        try:
            if a == a:
                await ctx.send(embed = embeda) or await ctx.send(embed = embeda1) 
            if b == b:
                await ctx.send(embed = embedb) or await ctx.send(embed = embedb1)
            if c == c:
                await ctx.send(embed = embedc) or await ctx.send(embed = embedc1)
            if d == d:
                await ctx.send(embed = embedd) or await ctx.send(embed = embedd1)
            if e == e:
                await ctx.send(embed = embede) or await ctx.send(embed = embede1)

        finally:        
            driver.quit()
            
lvl()            
rem()
client.run("ODM0MzQ1MDc2MjU5MDI4OTkz.YH_iZw.E2Lr-lYLa5dp8u3xsGWyCQbyI")
