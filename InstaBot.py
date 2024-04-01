import discord
import time
import re
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')  # Access the DISCORD_BOT_TOKEN environment variable

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.reactions = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Smoke mid every day!')

@client.event
async def on_message(message):
    # Avoid responding to the bot's own messages and ensure message is not from a bot
    if message.author == client.user or message.author.bot:
        return

    # Define your URL matching regex patterns
    instagram_url_regex = re.compile(r'https://www\.instagram\.com/reel/([a-zA-Z0-9_-]+)/')
    tiktok_url_regex = re.compile(r'https://www\.tiktok\.com/(.+)')

    # Instagram link processing
    instagram_matches = instagram_url_regex.search(message.content)
    if instagram_matches:
        timestamp = int(time.time())
        new_instagram_url = f'https://www.ddinstagram.com/reel/{instagram_matches.group(1)}/?ts={timestamp}'
        
        try:
            await message.delete()
            await message.channel.send(f'{message.author.mention} has shared an IG Reel! {new_instagram_url}')
        except Exception as error:
            print(f'Error deleting message or sending new Instagram message: {error}')

    # TikTok link processing for any URL
    tiktok_matches = tiktok_url_regex.search(message.content)
    if tiktok_matches:
        new_tiktok_url = f'https://www.vxtiktok.com/{tiktok_matches.group(1)}'

        try:
            await message.delete()
            await message.channel.send(f'{message.author.mention} has shared a TikTok video! {new_tiktok_url}')
        except Exception as error:
            print(f'Error deleting message or sending new TikTok message: {error}')

@client.event
async def on_reaction_add(reaction, user):
    # Check if the reaction is on a message sent by the bot
    if reaction.message.author.id != client.user.id:
        return

    # Check if the reaction is a thumbs down emoji
    if str(reaction.emoji) == '👎':
        message = reaction.message
        content = message.content

        try:
            await message.delete()
            await reaction.message.channel.send(content)
        except Exception as error:
            print(f'Error handling thumbs down reaction: {error}')

client.run(TOKEN)
