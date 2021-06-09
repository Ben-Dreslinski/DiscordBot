import discord
from discord.ext import commands
from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pathlib import Path
from lib.bingo import Bingo

PREFIX = "-"
OWNER_IDS = [119293628832153600]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def run(self, version):
        self.VERSION = version
        # path = Path(__file__).parent / "token.0"
        # self.TOKEN = path.read_text()
        with open("lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()
        
        print("running bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("bot connected")
    
    async def on_disconnect(self):
        print("bot disconnected")
    
    async def on_ready(self):
        if (not self.ready):
            self.ready = True
            self.stdout = self.get_channel(849398797535936522)
            self.guild = self.get_guild(836374591953174528)
            board = Bingo()
            await self.stdout.send(file=discord.File('lib/bingo/BINGOedit.png'))
            print("bot ready")
            await self.change_presence(activity=discord.Game('-commands'))
        else:
            print("bot reconnected")

    def updatesquare(self):
        @self.bot.command(name='updatesquare')
        async def command(self, letter: str, square: int):
            await self.stdout.send("letter: ", letter, "square: ", square)

bot = Bot()
board = Bingo()

@bot.command(name='green')
async def green(ctx, letter, square: int):
    board.greenUpdate(letter, square)
    await bot.stdout.send(file=discord.File('lib/bingo/BINGOedit.png'))

@bot.command(name='red')
async def red(ctx, letter, square: int):
    board.redUpdate(letter, square)
    await bot.stdout.send(file=discord.File('lib/bingo/BINGOedit.png'))

@bot.command(name='showboard')
async def showboard(ctx):
    await bot.stdout.send(file=discord.File('lib/bingo/BINGOedit.png'))

@bot.command(name='commands')
async def commands(ctx):
    myEmbed = discord.Embed(title="Commands", description="Last updated 6/2/2021", color=0x00ff00)
    myEmbed.add_field(name="Current Version", value=bot.VERSION, inline=False)
    myEmbed.add_field(name="-green <letter> <square>", value="Change square on the board to green", inline=False)
    myEmbed.add_field(name="-red <letter> <square>", value="Change square on the board to red", inline=False)
    myEmbed.add_field(name="-showboard", value="Displays current board", inline=False)
    myEmbed.add_field(name="starttime", value="Shows when the current board was generated", inline=False)
    myEmbed.set_footer(text="Future releases: idk suggest something")
    myEmbed.set_author(name="bendy")

    await bot.stdout.send(embed=myEmbed)

@bot.command(name='starttime')
async def commands(ctx):
    await bot.stdout.send("The current board was generated on " + board.getStartDate() + " at " + board.getStartTime())