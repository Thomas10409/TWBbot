import os
import json
import discord
from discord.commands import Option
from discord.ext import commands

class admin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.slash_command(name="update_state",description="更新狀態")
    async def update_state(self,ctx):
        with open("./config/author.json",encoding="utf-8") as fr:
            bot_author = json.loads(fr.read())
            if str(ctx.author) == bot_author["bot_author"]:
                with open("./config/state.json",encoding="utf-8") as f:
                    state = f.read()
                    state = json.loads(state)
                    status_w = state["state"]
                    activity_w = discord.Activity(type=discord.ActivityType.watching, name=state["state_text"])
                    await self.bot.change_presence(status= status_w, activity=activity_w)
                    await ctx.send_response(content="好歐",ephemeral=True)
            else:
                await ctx.send_response(content="笑死你沒權限",ephemeral=True)

def setup(bot):
    bot.add_cog(admin(bot))
    print("admin功能集被載入了")

def teardown(bot):
    print("admin功能集被卸載了")