import discord
import logging

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


client.run(config.token)
