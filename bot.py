import discord
import logging

from discord import Game

# very secure and secret file,.... ssshhhh
import config

# client configuration
client = discord.Client()

# logging configuration
LOGGING_FORMAT = \
'[%(asctime)s] - [%(levelname)s] - [%(funcName)s] - %(message)s'

logging.basicConfig(
    level=logging.INFO,
    format=LOGGING_FORMAT
)


@client.event
async def on_ready():
    logging.info("Bot logged in successfully!")
    client.change_presence(game=Game(name="What an amazing Python bot!"))

@client.event
async def on_message(message):
    logging.info("I got following message: " + message.content + " | by " + message.author.name)


client.run(config.token)
