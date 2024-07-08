import discord
from discord.ext import commands
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Se ha logueado {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy {bot.user}! bienvenido denuevo')

@bot.command()
async def chau(ctx):
    await ctx.send(f'Nos vemos pronto!')

@bot.command()
async def password(ctx, count_heh = 5):
    await ctx.send(gen_pass (10))

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def cool1(ctx):
    await ctx.send('Yes, El_Admin#0714 is cool.')

bot.run("MTI1NzM5Mjc5MzMyNDg4NDA4OA.Gx-Vgr.Rchlyc00LZNv7aZ9yiJToO3zhAPqv4i5UMuHks")