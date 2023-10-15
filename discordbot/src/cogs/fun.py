import discord
from discord.ext import commands
from config import COLOUR, CURRENCY, PREFIX

from func import load_file, savememdata, MEMDATA
from func import balance_give, balance_take
from func import check_acc, sufficient, validate
import time
from random import randint, choice

import traceback

SPAM = 'C:\\Users\\Adrian\\git\\Anima\\discordbot\\src\\data\\spamlist.txt'

'''
member = ctx.author
avatar = member.avatar.url
cogname = ctx.cog.qualified_name
colour = EMBED_COLOUR[str(ctx.cog.qualified_name)]
'''


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def spam(self, ctx, member: discord.Member = None):
        spamlist = load_file(SPAM)
        if member == None:
            member = ctx.author

        for idx in range(15):
            message = spamlist[randint(0, len(spamlist)-1)]
            await ctx.send(f'<@{member.id}> {message}')
            time.sleep(0.75)

    @commands.command(aliases=['gaydar'])
    async def howgay(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        avatar = member.avatar.url

        gen = randint(1, 25)
        print(f'gen: {gen}')
        try:
            if gen == 1:
                gay = randint(-100, 0)
            elif gen >= 9 and gen <= 11:
                gay = f'**69**'
            elif gen == 20 or gen == 21:
                gay = randint(100, 200)
            elif gen == 22:
                gay = randint(200, 500)
            else:
                gay = randint(0, 100)

            print(f'gay: {gay}.')
        except Exception as e:
            print(e)
            traceback.print_stack()

        embed = discord.Embed(
            description=f'**{member}** is {gay}% gay.', color=COLOUR['Fun'])
        await ctx.send(embed=embed)

    @commands.command(aliases=['bf', 'flip', 'coinflip'])
    async def betflip(self, ctx, predictin, amount=None):
        try:
            if await validate(ctx, ctx.author, 'wallet', amount) == True:

                heads = ['heads', 'head', 'h']
                tails = ['tails', 'tail', 't']

                if predictin.lower() in heads:
                    predict = 'heads'
                elif predictin.lower() in tails:
                    predict = 'tails'
                else:
                    embed = discord.Embed(
                        title='Invalid Inputs', color=COLOUR['Fail'])
                    embed.add_field(
                        name='Usage', value='``!betflip [predict] [bet amount]`` ``!betflip heads 1``', inline=False)
                    embed.add_field(
                        name='Aliases', value='``!bf``, ``!flip``', inline=True)
                    embed.add_field(
                        name='Predictions', value='"heads", "head", "h", "tails", "tail", "t"', inline=True)
                    await ctx.send(embed=embed)
                    return

                sides = ['heads', 'tails']
                result = sides[randint(0, 1)]
                print(f'result: {result}')

                if result == 'heads':
                    url = 'https://clipart-library.com/images_k/quarter-transparent-background/quarter-transparent-background-19.png'
                else:

                    url = 'https://clipart-library.com/images_k/quarter-transparent-background/quarter-transparent-background-7.png'

                if predict == result:
                    payout = int(amount)*2
                    print(f'payout: {payout}')
                    if balance_give(ctx, ctx.author, 'wallet', payout) == True:

                        embed = discord.Embed(
                            title=f'Coin Flip - {result}', description=f'**{ctx.author}** won  {CURRENCY} {payout}!', color=COLOUR['Fun'])
                        embed.set_thumbnail(url=url)

                else:
                    if balance_take(ctx, ctx.author, 'wallet', amount) == True:

                        embed = discord.Embed(
                            title=f'Coin Flip - {result}', description=f'**{ctx.author}** lost  {CURRENCY} {amount}!', color=COLOUR['Fun'])
                        embed.set_thumbnail(url=url)
                savememdata()
                await ctx.send(embed=embed)

        except Exception as e:
            print(e)
            traceback.print_stack()

    @commands.command()
    async def ahegao(self, ctx):
        await ctx.send(f'''
⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿''')


try:
    async def setup(client):
        await client.add_cog(Fun(client))
except Exception as e:
    print(e)
    traceback.print_stack()
