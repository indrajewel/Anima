import discord
from discord.ext import commands


async def sendmsg(ctx, member: discord.Member=None):
    print(member)
    if member == None:
        member = ctx.author

    if member == ctx.author:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name='No bank account found',
                        value=f'You do not have a bank account. Please open an account with ``!open_account``', inline=True)
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name='No bank account found',
                        value=f'{member} does not have a bank account. Please open an account with ``!open_account``', inline=True)
        await ctx.send(embed=embed)


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

    @commands.command()
    async def testmsg(self, ctx, user: discord.Member=None):
        if user == None:
            user = ctx.author

        await ctx.send('test')

        embed = discord.Embed(title='test dm', color=0xff0000)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
        embed.add_field(name='', value=f'message {member}', inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    async def nestedmsg(self, ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author
        await sendmsg(ctx, member)


async def setup(client):
    await client.add_cog(Test(client))
