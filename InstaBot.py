import discord
import time
import re
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the Discord bot token from environment variables
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Define regular expressions for matching Instagram and TikTok URLs
instagram_url_regex = re.compile(r"https://www\.instagram\.com/reel/([a-zA-Z0-9_-]+)/")
tiktok_url_regex = re.compile(r"https://www\.tiktok\.com/(.+)")

# Discord client setup with required intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.reactions = True
client = discord.Client(intents=intents)

# Event handler for bot initialization
@client.event
async def on_ready():
    print("📽️ InstaBot is running")

# Event handler for processing incoming messages
@client.event
async def on_message(message):
    # Avoid responding to the bot's own messages or other bots' messages
    if message.author == client.user or message.author.bot:
        return

    # Check for Instagram URLs in the message content
    instagram_matches = instagram_url_regex.search(message.content)
    if instagram_matches:
        timestamp = int(time.time())
        new_instagram_url = f"https://www.ddinstagram.com/reel/{instagram_matches.group(1)}/?ts={timestamp}"

        try:
            # Delete the original message and send a new message with the modified Instagram URL
            await message.delete()
            await message.channel.send(
                f"{message.author.mention} has shared an IG Reel! {new_instagram_url}"
            )
        except Exception as error:
            print(f"Error deleting message or sending new Instagram message: {error}")

    # Check for TikTok URLs in the message content
    tiktok_matches = tiktok_url_regex.search(message.content)
    if tiktok_url_regex.search(message.content):
        new_tiktok_url = f"https://www.vxtiktok.com/{tiktok_matches.group(1)}"

        try:
            # Delete the original message and send a new message with the modified TikTok URL
            await message.delete()
            await message.channel.send(
                f"{message.author.mention} has shared a TikTok video! {new_tiktok_url}"
            )
        except Exception as error:
            print(f"Error deleting message or sending new TikTok message: {error}")

# Event handler for processing reactions added to messages
@client.event
async def on_reaction_add(reaction, user):
    # If the reaction is a thumbs down and the message is sent by the bot, resend the message
    if str(reaction.emoji) == "👎" and reaction.message.author.id == client.user.id:
        message = reaction.message
        content = message.content

        try:
            # Delete the original message and resend it
            await message.delete()
            await reaction.message.channel.send(content)
        except Exception as error:
            print(f"Error handling thumbs down reaction: {error}")

# Run the bot
client.run(TOKEN)
