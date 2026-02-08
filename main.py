import discord
from discord.ext import commands

# Replace with your actual token if not using .env
TOKEN = 'SECRET CODE'

intents = discord.Intents.default()
intents.message_content = True # This matches the toggle you flipped in the portal!

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is now online and ready for the portfolio!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

bot.run(TOKEN)