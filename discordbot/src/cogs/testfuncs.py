import discord
from discord.ext import commands

from func import no_acc, pos, err
import asyncio


class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def testdm(self, ctx, user: discord.Member=None):
        if user == None:
            user = ctx.author

        await ctx.send('test')

        embed = discord.Embed(title='test dm', color=0xff0000)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
        embed.add_field(name='', value='message', inline=True)

        await user.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def testmsg(self, ctx, user: discord.Member=None):
        if user == None:
            user = ctx.author

        await ctx.send('test')

        embed = discord.Embed(title='test dm', color=0xff0000)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
        embed.add_field(name='', value=f'message {member}', inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def nestedmsg(self, ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author
        await sendmsg(ctx, member)

    @commands.command()
    @commands.is_owner()
    async def noacc(self, ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author
        await no_acc(ctx, member)

    @commands.command()
    @commands.is_owner()
    async def check(self, ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author

        try:
            await check_acc(ctx, member)
        except:
            traceback.print_stack()

    @commands.command()
    @commands.is_owner()
    async def pos(self, ctx, amount):
        await check_pos(ctx, int(amount))

    @commands.command()
    @commands.is_owner()
    async def error(self, ctx):
        await err(ctx)

    '''
    @commands.command()
    @commands.is_owner()
    async def testreact(self, ctx):
        yas = '✔️'
        nay = '❌'

        yeno = ['✔️', '❌']

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in yesno
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)

        if str(reaction.emoji) == yas:
            embed = discord.Embed(color=0xc75757)
            embed.add_field(name='', value='testembed', inline=False)
            await ctx.send(embed=embed)
            return await ctx.send(embed=embed)

        # there's only two reactions, so if the above function didn't return, it means the second reaction (nay) was used instead
        await ctx.send("Cancelled")
    '''
    '''
    @commands.command()
    @commands.is_owner()
    async def testr(ctx):
        try:
            if message.content.startswith('$thumb'):
                channel = message.channel
                await channel.send('Send me that reaction, mate')

                def check(reaction, user):
                    return user == message.author and str(reaction.emoji) == ''

                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    await channel.send('')
                else:
                    await channel.send('')

        except Exception as e:
            print(e)
            traceback.print_stack()
    '''


async def setup(client):
    await client.add_cog(Test(client))
