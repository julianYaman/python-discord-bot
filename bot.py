import discord
import logging

from discord import Game, Embed
from commands import ping

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

commands = {
    "ping": ping
}


@client.event
async def on_ready() -> None:
    logging.info("Bot logged in successfully!")
    client.change_presence(game=Game(name="What an amazing Python bot!"))


@client.event
async def on_message(message) -> None:
    # logging.info("I got following message: " + message.content + " | by " + message.author.name)
    if message.content.startswith(config.prefix):
        command = message.content[1:].split(" ")[0]
        args = message.content.split(" ")[1:]
        # print("Command: %s\nArgs: %s" % (command, args.__str__()[1:-1].replace("'", "")))
        if commands.__contains__(command):
            logging.info(
                f"Got an valid command: '{command}' from {message.author.name} on this server: {message.server.name}")
            await commands.get(command).execute(args, message, client, command)
        else:
            await client.send_message(message.channel,
                                      embed=Embed
                                      (color=discord.Color.red(),
                                       description=f"The command {command} is not available!"))


client.run(config.token)
