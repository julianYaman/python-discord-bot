import discord
import logging

from discord import Game, Embed
from commands import cmd_help, cmd_ping

# very secure and secret file,.... ssshhhh
import config

# client configuration

client = discord.Client()

# logging configuration
LOGGING_FORMAT = '[%(asctime)s] - [%(levelname)s] - [%(funcName)s] - %(message)s -> %(filename)s'

logging.basicConfig(
    level=logging.INFO,
    format=LOGGING_FORMAT
)

commands = {
    "help": {
        "description": "With this command, you get this message showing all commands of this bot.",
        "script": cmd_help
    },
    "ping": {
        "description": "You guessed it!",
        "script": cmd_ping
    },
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
            # If command is help
            if command == "help":
                await commands.get(command).get("script").execute(args, message, client, command, commands)
            else:
                await commands.get(command).get("script").execute(args, message, client, command)
        else:
            await client.send_message(message.channel,
                                      embed=Embed
                                      (color=discord.Color.red(),
                                       description=f"The command **{command}** is not available!"))


client.run(config.token)
