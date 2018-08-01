import discord
import logging
import config
from typing import List, Optional
from discord import Embed


async def execute(args: List, message: discord.Message, client: discord.Client, command: str, *commands) -> None:

    if commands:

        embed = Embed(color=discord.Color.green(),
                      description="All commands of this bot:",)

        embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
        embed.set_footer(text="This command is in construction atm.")

        for cmd in commands[0].keys():
            embed.add_field(name=f"{config.prefix}{cmd}", value=commands[0].get(cmd).get("description"), inline=False)

        await client.send_message(message.channel,
                                  embed=embed)

    else:
        logging.critical("Issue in the execution of the command! No 'commands' argument given!")
        await client.send_message(message.channel,
                                  embed=Embed
                                  (color=discord.Color.red(),
                                   description=f"ERROR. There was a problem while executing the command. Sorry."))
