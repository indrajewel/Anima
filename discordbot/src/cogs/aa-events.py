import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from bottoken import TOKEN

import config
from func import load_file, savememdata
from func import memdata
from config import COLOUR


import os
import traceback


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        print(f'''{message.created_at} {message.author} ({message.author.id}) in {message.guild} #{message.channel}:
    "{message.content}"
    ''')
        await commands.process_commands(message)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            embed = discord.Embed(color=config.COLOUR['Fail'])
            embed.add_field(
                name='Command not found', value=f'Use ``{config.PREFIX}help`` to view available commands.', inline=True)
            await ctx.send(embed=embed)

        if error.__class__ is commands.MissingRequiredArgument:
            embed = discord.Embed(color=config.COLOUR['Fail'])
            embed.add_field(
                name='Invalid Inputs', value=f'Check parameters.', inline=True)
            await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # channel = client.get_channel(1155931099357253672)
        userid = member.id
        print(f'{member} ({userid}) joined {member.guild}')
        await member.send(f'{member} has joined the cosmic gnar gnar.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = client.get_channel(1155931099357253672)
        await channel.send(f'{member} has returned to void.')


async def setup(client):
    await client.add_cog(Events(client))
