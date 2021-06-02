from discord.ext import commands
from discord.ext.commands import Cog
import discord
from lib.bot import bot

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hello(self, ctx, *, args):
        await bot.stdout.send(args)

def setup(bot):
    bot.add_cog(fun(bot))