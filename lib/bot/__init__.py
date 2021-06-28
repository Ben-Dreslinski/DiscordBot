import discord
from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from lib.bingo import Bingo
import asyncio

PREFIX = "-"
OWNER_IDS = []

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def run(self, version):
        self.VERSION = version
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
            self.stdout = self.get_channel()
            self.guild = self.get_guild()
            await self.stdout.send(file=discord.File('lib/bingo/BINGOedit.png'))
            print("bot ready")
            await self.change_presence(activity=discord.Game('-commands'))
        else:
            print("bot reconnected")

bot = Bot()
board = Bingo()

@bot.command(name='green')
async def green(ctx, letter, square: int):
    result = board.greenUpdate(letter, square)
    if (result < 0):
        await bot.stdout.send('The free space is already green!')
    elif (result < 1):
        await bot.stdout.send(f'{letter.upper()} {square} is already a green square!')
    else:
        await bot.stdout.send(f'{letter.upper()} {square} was succesfully changed from red to green!')
        await bot.stdout.send(file=discord.File('lib/bingo/BINGOedit.png'))

@bot.command(name='red')
async def red(ctx, letter, square: int):
    result = board.redUpdate(letter, square)
    if (result < 0):
        await bot.stdout.send('The free space is always green and cannot be changed to red!')
    elif (result < 1):
        await bot.stdout.send(f'{letter.upper()} {square} is already a red square!')
    else:
        await bot.stdout.send(f'{letter.upper()} {square} was succesfully changed from green to red!')
        await bot.stdout.send(file=discord.File('lib/bingo/BINGOedit.png'))

@bot.command(name='showboard')
async def showboard(ctx):
    await bot.stdout.send(file=discord.File('lib/bingo/BINGOedit.png'))

@bot.command(name='commands')
async def commands(ctx):
    myEmbed = discord.Embed(title="Commands", description="Last updated 6/27/2021", color=0x00ff00)
    myEmbed.add_field(name="Current Version", value=bot.VERSION, inline=False)
    myEmbed.add_field(name="-green <letter> <square>", value="Change square on the board to green", inline=False)
    myEmbed.add_field(name="-red <letter> <square>", value="Change square on the board to red", inline=False)
    myEmbed.add_field(name="-showboard", value="Displays current board", inline=False)
    myEmbed.add_field(name="-starttime", value="Shows when the current board was generated", inline=False)
    myEmbed.add_field(name='-newboard', value='Creates a new board and discards the old one, cannot be undone', inline=False)
    myEmbed.set_author(name="bendy")

    await bot.stdout.send(embed=myEmbed)

@bot.command(name='starttime')
async def commands(ctx):
    await bot.stdout.send(f'The current board was generated on {board.getStartDate()} at {board.getStartTime()} UTC.')

@bot.command(name='newboard')
async def newBoard(ctx):
    await bot.stdout.send('This will create a new board which discards the old one and can NOT be undone, are you sure? (y/n)')

    try:
        message = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
    except asyncio.TimeoutError:
        await bot.stdout.send('Response timed out, aborting.')
    else:
        if (message.content.lower() == 'y'):
            await bot.stdout.send('Creating new board...')
            global board
            board.reset()
            await bot.stdout.send(file=discord.File('lib/bingo/BINGOedit.png'))
        elif (message.content.lower() == 'n'):
            await bot.stdout.send('The old board will be preserved')
        else:
            await bot.stdout.send('Response not recognized, aborting.')