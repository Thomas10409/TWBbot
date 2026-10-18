import os
import re
import json
import discord
from discord.ext import commands
from discord.commands import Option

bot = commands.Bot()
command_list = {}
load = []
unload = []

author_name = ""

def isYouTubeURL(youtube_url):
    youtube_regex = r"^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))(?P<YouTubeID>(\w|-){11})(?:\S+)?$"
    sreMatch = re.match(youtube_regex, youtube_url)
    return sreMatch.group("YouTubeID") if sreMatch else None

@bot.event
async def on_ready():
    print("Bot is online!")
    with open("./config/state.json",encoding="utf-8") as f:
        state = f.read()
        state = json.loads(state)
        status_w = state["state"]
        activity_w = discord.Activity(type=discord.ActivityType.watching, name=state["state_text"])
        await bot.change_presence(status= status_w, activity=activity_w)
    with open("./config/author.json",encoding="utf-8") as f:
        data = f.read()
        data = json.loads(state)
        author_name = state["bot_author"]

@bot.slash_command(name="help",description="給你看看指令的用法")
async def help(ctx):
    embed=discord.Embed(title="指令列表", description="這裡的指令都可以用", color=0x1bff00)
    embed.set_author(name="Twmc Bot", icon_url="https://i.imgur.com/bn0i0aT.png")
    with open("./config/commands.json",encoding="utf-8") as f:
        command_info = f.read()
        command_info = json.loads(command_info)
        i = 1
        while(i != len(command_info)+1):
            embed.add_field(name=f"{command_info[str(i)][0]}",value=f"{command_info[str(i)][1]}", inline=command_info[str(i)][2])
            i += 1
    embed.add_field(name="有問題可以私訊我\n或加入我ㄉㄜDC群", value="[link]", inline=False)
    embed.set_footer(text=f"作者:{bot_author}")
    await ctx.respond(embed=embed)

print("Command Cogs:")
for filename in os.listdir("./commands"):
    if filename.endswith('.py'):
        print(f"    {filename}  ",end="")
        try:
            command_list[f"{filename[:-3]}"] = "ok"
            load.append(f"{filename[:-3]}")
            bot.load_extension(f"commands.{filename[:-3]}")
        except Exception as e:
            print(e)
            command_list[f"{filename[:-3]}"] = "error"
            unload.append(f"{filename[:-3]}")

print(f"commands: {command_list}")
print(f"sucess: {load}")
print(f"fail: {unload}")

with open('token.json', "r", encoding = "utf8") as file:
    data = json.load(file)

bot.run(data['token'])
