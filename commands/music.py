import re
import pafy
import asyncio
import discord
from discord.ext import commands
from discord.commands import Option

def isYouTubeURL(youtube_url):
        youtube_regex = r"^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))(?P<YouTubeID>(\w|-){11})(?:\S+)?$"
        sreMatch = re.match(youtube_regex, youtube_url)
        return sreMatch.group("YouTubeID") if sreMatch else None

class music(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.slash_command(name="加入語音",description="讓機器人加入語音")
    @commands.cooldown(3, 2)
    async def join(self,ctx):
        vc = ctx.voice_client
        if ctx.author.voice != None:
            try:
                if vc == None:
                    await ctx.author.voice.channel.connect()
                else:
                    if vc.is_playing == True:
                        await vc.stop()
                    await vc.move_to(ctx.author.voice.channel)
                await ctx.send_response(content=f"{vc}")
            except Exception as e:
                await ctx.send_response(content=f"出了點問題,不如晚點再試試?\n錯誤內容:\n```{e}```")
        else:
            await ctx.send_response(content="可以先加入一個語音頻道再叫我加嗎\n我不會讀心術")

    @commands.slash_command(name="離開語音",description="讓機器人退出語音")
    @commands.cooldown(3, 2)
    async def leave(self,ctx):
        vc = ctx.voice_client
        if ctx.author.voice != None:
            try:
                if vc != None:
                    await vc.disconnect()
                else:
                    await ctx.send_response(content="我好像沒有加入任何一個語音頻道\n你趕我幹嘛")
                await ctx.send_response(content=f"{vc}")
            except Exception as e:
                await ctx.send_response(content=f"出了點問題,不如晚點再試試?\n錯誤內容:\n```{e}```")
        else:
            await ctx.send_response(content="可以先加入你要我退的語音再叫我嗎\n我不會讀心術")

def setup(bot):
    bot.add_cog(music(bot))

def teardown(bot):
    print("music功能集被卸載了")