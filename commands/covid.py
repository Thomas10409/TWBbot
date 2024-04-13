import json
import time
import discord
import requests as req
from discord.ext import commands
from discord.commands import Option

class covid(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.api = "https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=4048"
    @commands.slash_command(name="covid感染人數",description="獲取昨日確診人數")
    async def covid_get(self,ctx):
        await ctx.response.defer()
        headers = {'user-agent': 'Mozilla/5.0'}
        data = json.loads(req.get(self.api, headers=headers).text)[0]["a06"]
        embed=discord.Embed(color=0xff0000)
        embed.set_author(name="Covid-19", icon_url="https://i.imgur.com/aGMbSOl.png")
        embed.add_field(name="昨日確診數", value=f"{str(data)}人", inline=True)
        embed.set_footer(text="資料來源:covid-19.nchc.org.tw")
        await ctx.followup.send(embed=embed)

def setup(bot):
    bot.add_cog(covid(bot))
    print("covid功能集被載入了")

def teardown(bot):
    print("covid功能集被卸載了")