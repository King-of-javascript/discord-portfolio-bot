import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# 1. Load the hidden .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2. Safety Check (This helps us catch the NoneType error early)
if TOKEN is None:
    print("❌ ERROR: No token found! Check if your file is named exactly '.env'")
    exit()

# 3. Bot Setup
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ SUCCESS: {bot.user.name} is now online!')
    print(f'Logged in as ID: {bot.user.id}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

# 4. Start the Bot
bot.run(TOKEN)
