import discord
from discord.ext import commands
from config import COLOUR, CURRENCY

from func import MEMDATA, BADWORDS, SPAM
from func import memdata, badwords, spamlist
from func import load_file, savememdata, gen_rand, balance_give, balance_take
from random import randint
import traceback


'''
member = ctx.author
avatar = member.avatar.url
cogname = ctx.cog.qualified_name
colour = embed_colour[str(cogname)]
'''


def gen_card():
    issuers = ['4502', '4503', '4504', '4505', '4506']
    issuer = issuers[randint(0, len(issuers)-1)]

    account = f'{gen_rand(4)} {gen_rand(4)} {gen_rand(4)}'
    card = f'{issuer} {account}'

    month = randint(1, 12)
    if month < 10:
        month = f'0{month}'

    year = randint(23, 29)

    expiry = f'{month}/{year}'
    code = gen_rand(3)
    pin = gen_rand(4)

    return card, expiry, code, pin


class Bank(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def open_account(self, ctx):
        member = ctx.author
        avatar = member.avatar.url

        memdata = load_file(MEMDATA)

        if 'wallet' in memdata[member.id]:
            wallet = memdata[str(ctx.author.id)]['wallet']
            bank = memdata[str(ctx.author.id)]['bank']

            embed = discord.Embed(
                title='Account Already Exists', color=COLOUR['Bank'])
            embed.set_author(name=member, icon_url=avatar)
            embed.add_field(name='Wallet', value=f'${wallet}', inline=True)
            embed.add_field(name='Bank', value=f'${bank}', inline=True)
            await ctx.send(embed=embed)

        else:
            memdata[str(member.id)]['wallet'] = 10
            memdata[str(member.id)]['bank'] = 500
            savememdata()

            wallet = memdata[str(ctx.author.id)]['wallet']
            bank = memdata[str(ctx.author.id)]['bank']

            embed = discord.Embed(
                title='Bank Account Opened', color=COLOUR['Bank'])
            embed.set_author(name=member, icon_url=avatar)
            embed.add_field(
                name='Wallet', value=f'{CURRENCY} {wallet}', inline=True)
            embed.add_field(
                name='Bank', value=f'{CURRENCY} {bank}', inline=True)
            await ctx.send(embed=embed)

        await ctx.send(f'Account opened. {ctx.author} wallet: {wallet} bank: {bank}')

    @commands.command(aliases=['award'])
    async def bal_award(self, ctx, amount, member: discord.Member = None):
        if member == None:
            member = ctx.author

        print(member, member.id)

        await balance_give(member, 'bank', int(amount), ctx)
        savememdata()

    @commands.command(aliases=['take', 'seize'])
    async def bal_take(self, ctx, amount=None, member: discord.Member = None):
        if member == None:
            member = ctx.author

        if amount > 0:
            try:
                balance_take(member, 'bank', int(amount))
                savememdata()

                embed = discord.Embed(title='Funds Seized',
                                      color=COLOUR['Bank'])
                embed.set_author(name=member, icon_url=member.avatar.url)
                embed.add_field(
                    name='', value=f"Seized  {CURRENCY} {amount} from {member}'s bank account.", inline=True)
                await ctx.send(embed=embed)
            except Exception as e:
                traceback.print_tb(e.__traceback__)
                print(e)

        else:
            print(f'**')
        print(member, member.id)

        try:
            balance_take(member, 'bank', int(amount))
            savememdata()

            embed = discord.Embed(title='Funds Seized',
                                  color=COLOUR['Bank'])
            embed.set_author(name=member, icon_url=member.avatar.url)
            embed.add_field(
                name='', value=f"Seized  {CURRENCY} {amount} from {member}'s bank account.", inline=True)
            await ctx.send(embed=embed)
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            print(e)

    @commands.command(aliases=['d'])
    async def deposit(self, ctx, amount):
        balance_take(ctx.author, 'wallet', amount)
        balance_give(ctx.author, 'bank', amount)

    @commands.command(aliases=['w'])
    async def widthdraw(self, ctx, amount):
        balance_give(ctx.author, 'bank', amount)
        balance_take(ctx.author, 'wallet', amount)

    @commands.command(aliases=['bal'])
    async def balance(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        memdata = load_file(MEMDATA)
        avatar = member.avatar.url

        try:
            wallet = memdata[str(member.id)]['wallet']
            bank = memdata[str(member.id)]['bank']

            embed = discord.Embed(title='Balance', color=COLOUR['Bank'])
            embed.set_author(name=member, icon_url=avatar)
            embed.add_field(
                name='Wallet', value=f'{CURRENCY} {wallet}', inline=True)
            embed.add_field(
                name='Bank', value=f'{CURRENCY} {bank}', inline=True)
            await ctx.send(embed=embed)

        except KeyError:
            await ctx.send('No bank account found. Please open account with ``!open_account``.')

    @commands.command(aliases=['give'])
    async def etransfer(self, ctx, amount, member: discord.Member = None):
        if member == None:
            member = ctx.author

        '''
    
        try
            load memdata
            if author in memdata
            
                if member in memdata
                    
                    if amount > 0
                        bal_take
                        
                        bal_give
                        
                        
                        embed
                        print
                    
                    elif amount < balance
                        insufficient funds
                        
                    else

                else
                    member not found
            
            else
                author not found
                
            
            else
                
        except
            input error
        '''

        title = 'e-Transfer'

        load_file(MEMDATA)

        try:
            sender_bal = memdata[str(ctx.author.id)]['bank']
        except:
            message = f'No bank account found for sender {ctx.author}'
            print(message)

        try:
            recipient_bal = memdata[str(member.id)]['bank']
        except:

            message
            print(f'No bank account found for recipient {member}')
            return

        if member == None:
            member = ctx.author
            avatar = member.avatar.url

            # please choose member to e-transfer
            print('No member selected')
            return

        elif int(amount) <= 0:
            # amount must be greater than 0
            print('Cannot send <= 0')
            return

        else:
            amount = int(amount)
            if sender_bal < amount:
                # insufficient funds
                print('insufficient funds')
                return
            else:
                sender_bal += - amount
                recipient_bal += amount
                # e-transfer sent
                print(f'{ctx.author} sent ${amount} to {member}')
                savememdata()

        embed = discord.Embed(title='e-Transfer Success', color=COLOUR['Bank'])
        embed.set_author(name=member, icon_url=avatar)
        embed.add_field(name='From', value=ctx.author, inline=True)
        embed.add_field(name='To', value=member, inline=True)
        embed.add_field(
            name=f'Amount', value=f'{CURRENCY} {amount}', inline=True)

        await ctx.send(embed=embed)

    @commands.command
    async def drop(self, ctx):
        pass

    @commands.command(aliases=['getcc'])
    async def getcard(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        avatar = member.avatar.url

        card = gen_card()

        number = card[0]
        expiry = card[1]
        code = card[2]
        pin = card[3]

        embed = discord.Embed(
            title=f'Card Details', color=COLOUR['Bank'])
        embed.set_author(name=member, url=None, icon_url=avatar)
        embed.add_field(name='Number', value=number, inline=False)
        embed.add_field(name='Expiry', value=expiry, inline=True)
        embed.add_field(name='Code', value=code, inline=True)
        embed.add_field(name='Pin', value=pin, inline=True)
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Bank(client))
