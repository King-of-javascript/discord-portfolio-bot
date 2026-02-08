import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

# --- 1. THE "KEEP ALIVE" WEB SERVER ---
app = Flask('')

@app.route('/')
def home():
    return "I am alive and hosting the portfolio bot!"

def run():
    # Render uses port 10000 by default for free web services
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True # This ensures the thread dies when the main script stops
    t.start()

# --- 2. BOT SETUP ---
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    print("❌ ERROR: No token found!")
    exit()

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ SUCCESS: {bot.user.name} is now online!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

# --- 3. START BOTH ---
if __name__ == "__main__":
    keep_alive()  # Starts the web server in the background
    bot.run(TOKEN) # Starts the Discord bot