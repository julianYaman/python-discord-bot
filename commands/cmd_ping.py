import discord
from typing import List, Optional


async def execute(args: List, message, client, command: str) -> None:
    await client.send_message(message.channel, f"Pong!")
