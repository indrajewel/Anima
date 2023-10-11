import discord
from discord.ext import commands


class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def testdm(self, ctx, user: discord.Member=None):
        if user == None:
            user = ctx.author

        await ctx.send('test')
        embed = discord.Embed(title='test dm', color=0xff0000)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
        embed.add_field(name='', value='message', inline=True)
        await user.send(embed=embed)


async def setup(client):
    await client.add_cog(Test(client))
