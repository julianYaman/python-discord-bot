import discord
import logging
from typing import List, Optional
from discord import Embed


async def execute(args: List, message, client, command: str, *commands) -> None:

    if commands:
        help_description = ""

        for cmd in commands[0].keys():
            help_description = help_description + f"**-{cmd}**\n\n"

        await client.send_message(message.channel,
                                  embed=Embed(color=discord.Color.green(),
                                              description=help_description,
                                              title="All commands:"))

    else:
        logging.critical("Issue in the execution of the command! No 'commands' argument given!")
        await client.send_message(message.channel,
                                  embed=Embed
                                  (color=discord.Color.red(),
                                   description=f"ERROR. There was a problem while executing the command. Sorry."))
