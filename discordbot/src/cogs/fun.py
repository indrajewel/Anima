import discord
from discord.ext import commands
from config import COLOUR, CURRENCY, PREFIX

# from func import memdata, badwords, spamlist, balance_give, balance_take
from func import load_file, savememdata
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

        gay = randint(0, 100)

        embed = discord.Embed(color=COLOUR['Fun'])
        embed.set_author(name=member, icon_url=avatar)
        embed.add_field(name='', value=f'{member} is {gay}% gay.', inline=True)
        await ctx.send(embed=embed)

    @commands.command(aliases=['bf', 'flip', 'coinflip'])
    async def betflip(self, ctx, predictin, amount=None):

        '''
        heads = ['heads', 'head', 'h']
        tails = ['tails', 'tail', 't']

        if predictin.lower() in heads:
            predictin = 'heads'
        elif predictin.lower() in tails:
            predictin = 'tails'

        sides = ['heads', 'tails']
        result = choice(sides)

        if predictin == result:
            payout = int(amount)*2
            print(f'payout: {payout}')

            balance_give(ctx, ctx.author, 'wallet', payout)

            embed = discord.Embed(title='Coin Flip', color=colour)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
            embed.add_field(name='', value=f'Flipped {result}', inline=False)
            embed.add_field(name='', value=f'{ctx.author} won  {CURRENCY}{payout}!', inline=False)
            await ctx.send(embed=embed)




        if predictin == None

        elif (check_acc() and sufficient() )
            if bank true

            else
                error bank not found

        elif amount > balance
            insufficienr funds

        else
            unknown err

        OR
        0 < amount < balance

        if amount > 0
            try:
                if bank true
                    flip

                    if predict true
                        award

                    else
                        remove

                else
                    bank error not exist

            except

        else
            regular flip


        '''

        '''
        if amount > 0:
            try:
                wallet = memdata[str(ctx.author.id)]['wallet']

                if int(amount) <= 0:
                    await ctx.send(f'invalid bet amount. must be > 0')
                    embed = discord.Embed(
                        title='', color=COLOUR['Fail'])
                    embed.add_field(
                        name='Invalid Bet Amount', value=f"Bet must be greater than {CURRENCY}0", inline=False)
                    await ctx.send(embed=embed)

                    return
                elif int(amount) > wallet:
                    print(wallet)

                    await ctx.send(f'insufficient funds')

                    embed = discord.Embed(
                        title='Insufficient Funds', color=COLOUR['Fail'])
                    embed.add_field(
                        name='Wallet Balance', value=f"{CURRENCY}{wallet}", inline=False)
                    await ctx.send(embed=embed)
                    return

                else:

                    sides = ['h', 't']
                    result = choice(sides)

                    print(f'result:{result}')

                    try:
                        if predict.lower() == result:
                            payout = int(amount)*2
                            print(f'payout {payout}')

                            balance_give(ctx.author, 'wallet', payout)

                            embed = discord.Embed(
                                title='Coin Flip', color=colour)
                            embed.set_author(
                                name=ctx.author, icon_url=ctx.author.avatar.url)
                            embed.add_field(
                                name='', value=f'Flipped {result}', inline=False)
                            embed.add_field(
                                name='', value=f'{ctx.author} won  {CURRENCY}{payout}!', inline=False)
                            await ctx.send(embed=embed)

                        else:
                            balance_take(ctx.author, 'wallet', amount)

                    except:
                        print(f'failed check')

                    # savememdata()

            except Exception as e:
                print('failed all')
                traceback.print_stack()

                await ctx.send('failed')

                embed = discord.Embed(color=0xff0000)
                embed.add_field(
                    name='Invalid Input', value=f'Example: ``{PREFIX}betflip heads 5``', inline=False)
                await ctx.send(embed=embed)
        
        '''
        if (predictin or amount) == None:

            # invalid Input
            embed = discord.Embed(title='Invalid Input', color=COLOUR['Fail'])
            embed.add_field(
                name='', value=f'Usage: ``{PREFIX}betflip [prediction] [bet amount]``', inline=False)
            embed.add_field(
                name='', value=f'Example: ``{PREFIX}betflip heads 5``', inline=False)
            await ctx.send(embed=embed)

            print(f'predictin: {predictin}')
            predict = predictin[0]
            print(f'predict: {predict}')
            print(amount)
            return

        else:
            try:
                wallet = memdata[str(ctx.author.id)]['wallet']

                if int(amount) <= 0:
                    await ctx.send(f'invalid bet amount. must be > 0')
                    embed = discord.Embed(
                        title='', color=COLOUR['Fail'])
                    embed.add_field(
                        name='Invalid Bet Amount', value=f"Bet must be greater than {CURRENCY}0", inline=False)
                    await ctx.send(embed=embed)

                    return
                elif int(amount) > wallet:
                    print(wallet)

                    await ctx.send(f'insufficient funds')

                    embed = discord.Embed(
                        title='Insufficient Funds', color=COLOUR['Fail'])
                    embed.add_field(
                        name='Wallet Balance', value=f"{CURRENCY}{wallet}", inline=False)
                    await ctx.send(embed=embed)
                    return

                else:

                    sides = ['h', 't']
                    result = choice(sides)

                    print(f'result:{result}')

                    try:
                        if predict.lower() == result:
                            payout = int(amount)*2
                            print(f'payout {payout}')

                            balance_give(ctx.author, 'wallet', payout)

                            embed = discord.Embed(
                                title='Coin Flip', color=COLOUR['Fun'])
                            embed.set_author(
                                name=ctx.author, icon_url=ctx.author.avatar.url)
                            embed.add_field(
                                name='', value=f'Flipped {result}', inline=False)
                            embed.add_field(
                                name='', value=f'{ctx.author} won  {CURRENCY}{payout}!', inline=False)
                            await ctx.send(embed=embed)

                        else:
                            balance_take(ctx.author, 'wallet', amount)

                    except:
                        print(f'failed check')

                    # savememdata()

            except Exception as e:
                print('failed all')
                traceback.print_stack()

                await ctx.send('failed')

                embed = discord.Embed(color=0xff0000)
                embed.add_field(
                    name='Invalid Input', value=f'Example: ``{PREFIX}betflip heads 5``', inline=False)
                await ctx.send(embed=embed)

            pass


async def setup(client):
    await client.add_cog(Fun(client))
