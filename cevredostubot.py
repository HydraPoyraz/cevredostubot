import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def whats_app(ctx):
    await ctx.send("ben iyiyim")
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTE2NDk3MjE1NDM2Njk5NjU2MQ.G-L-NK.q05LGwlPE6255bT1OfTC3oIIjvTZGD700-V5yU")
