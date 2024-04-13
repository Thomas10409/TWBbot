import base64
import discord
import hashlib
from discord.ext import commands
from discord.commands import Option

class encrypt(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.slash_command(name="base64_enc",description="把文字用base64加密")
    async def base64_enc(self,ctx,arg: Option(str,"輸入你要加密的", default='', required=True)):
        input_str = arg.encode("UTF-8")
        input_str = base64.b64encode(input_str)
        await ctx.send_response(content=f"你的加密結果: {input_str.decode('UTF-8')}",ephemeral=True)
        
    @commands.slash_command(name="base64_dec",description="把base64解密成文字")
    async def base64_enc(self,ctx,arg: Option(str,"輸入你要解密的", default='', required=True)):
        input_str = arg.encode("UTF-8")
        input_str = base64.b64decode(input_str)
        await ctx.send_response(content=f"你的解密結果: {input_str.decode('UTF-8')}",ephemeral=True)
        
    @commands.slash_command(name="hash",description="計算文字的哈希值")
    async def hash(self,ctx,arg: Option(str,"輸入你要計算的", default='', required=True)):
        out = hashlib.md5(f'{arg}'.encode('utf-8')).hexdigest()
        await ctx.send_response(content=f"你的計算結果: {out}",ephemeral=True)

def setup(bot):
    bot.add_cog(encrypt(bot))
    print("encrypt功能集被載入了")

def teardown(bot):
    print("encrypt功能集被卸載了")