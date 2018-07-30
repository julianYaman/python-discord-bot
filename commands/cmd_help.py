import discord
from typing import List
from discord import Embed


# Work in progress
async def execute(args: List, message, client, command: str) -> None:

    await client.send_message(message.channel,
                              embed=Embed(color=discord.Color.green(),
                                          description="Help command"))
