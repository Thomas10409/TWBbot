import discord
from discord.ext import commands

class funny(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.slash_command(name="rickroll",description="字面意思")
    async def rickroll(self,ctx):
        await ctx.respond("Yo! 你被rick_roll了\nhttps://i.imgflip.com/4whwu5.gif")

def setup(bot):
    bot.add_cog(funny(bot))
    print("funny功能集被載入了")

def teardown(bot):
    print("funny功能集被卸載了")
