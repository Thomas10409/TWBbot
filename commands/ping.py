import discord
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="ping",description="獲取機器人的延遲")
    async def ping(self, ctx):
        embed=discord.Embed(title="延遲:", description="Ping:" + str(round(self.bot.latency*1000)) + "ms", color=0x2bff00)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(ping(bot))
    print("ping功能集被載入了")

def teardown(bot):
    print("ping功能集被卸載了")

