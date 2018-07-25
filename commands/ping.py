import discord


async def execute(args, message, client, command):
    await client.send_message(message.channel, "Pong!")
