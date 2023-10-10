import discord
from discord.ext import commands


class cog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send('test')


async def setup(client):
    await client.add_cog(cog(client))
