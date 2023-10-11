import discord
from discord.ext import commands
from config import COLOUR, CURRENCY, PREFIX

from func import MEMDATA
from func import memdata
from func import load_file, savememdata
from func import gen_rand, check_acc, valid_amount
from func import balance_give, balance_take

from func import no_acc, err
from func import invalidmem
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

        if await check_acc(ctx, member) == True:
            wallet = memdata[str(ctx.author.id)]['wallet']
            bank = memdata[str(ctx.author.id)]['bank']

            # DM EMBED
            embed = discord.Embed(
                title='Account Already Exists', color=COLOUR['Bank'])
            embed.set_author(name=member, icon_url=avatar)
            embed.add_field(
                name='Wallet', value=f'{CURRENCY} {wallet}', inline=True)
            embed.add_field(
                name='Bank', value=f'{CURRENCY} {bank}', inline=True)
            await member.send(embed=embed)

            # PUBLIC EMBED
            if isinstance(ctx.channel, discord.channel.DMChannel) == False:
                embed = discord.Embed(color=COLOUR['Bank'])
                embed.add_field(
                    name='', value=f'Account already exists.', inline=True)
                await ctx.send(embed=embed)
        else:
            print(memdata)
            memdata[str(member.id)]['wallet'] = 10
            memdata[str(member.id)]['bank'] = 200

            print(memdata)

            savememdata()

            wallet = memdata[str(ctx.author.id)]['wallet']
            bank = memdata[str(ctx.author.id)]['bank']

            # Send embed DM
            embed = discord.Embed(
                title='Bank Account Opened', color=COLOUR['Bank'])
            embed.set_author(name=member, icon_url=avatar)
            embed.add_field(
                name='Wallet', value=f'{CURRENCY} {wallet}', inline=True)
            embed.add_field(
                name='Bank', value=f'{CURRENCY} {bank}', inline=True)
            await member.send(embed=embed)
            print(memdata)
            print(f'**!open_account: {member} opened a bank account')

            # Send embed Public
            if isinstance(ctx.channel, discord.channel.DMChannel) == False:
                embed = discord.Embed(color=COLOUR['Bank'])
                embed.set_author(name=member, icon_url=member.avatar.url)
                embed.add_field(
                    name='', value=f'{member} opened a bank account!', inline=True)
                await ctx.send(embed=embed)

    @commands.command(aliases=['award'])
    async def bal_award(self, ctx, amount, member: discord.Member = None):
        print(f'**{PREFIX}bal_award')
        try:
            if member == None:
                member = ctx.author

            # if await check_acc(ctx, member) == True:
                # print(f'member, member.id')
                # await balance_give(ctx, member, 'bank', int(amount))

                await balance_give(ctx, member, 'bank', int(amount))

        except:
            print(f'a')
            traceback.print_stack()

    @commands.command(aliases=['take', 'seize'])
    async def bal_take(self, ctx, amount=None, member: discord.Member = None):
        if member == None:
            member = ctx.author

        print(member, member.id)

        if amount <= 0:
            balance_take(member, 'bank', int(amount), ctx)
            savememdata()

            embed = discord.Embed(title='Funds Seized', color=COLOUR['Bank'])
            embed.set_author(name=member, icon_url=member.avatar.url)
            embed.add_field(
                name='', value=f"Seized  {CURRENCY} {amount} from {member}'s bank account.", inline=True)
            await ctx.send(embed=embed)

        if amount > 0:
            try:
                await balance_take(member, 'bank', int(amount), ctx)
                savememdata()

            except Exception as e:
                traceback.print_tb(e.__traceback__)
                print(e)

        else:
            print(f'**bal_take(): error')
        print(member, member.id)

        try:
            await balance_take(member, 'bank', int(amount))
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
        try:
            if check_acc(member) == True:

                print(f'True')

                try:
                    if amount <= 0:
                        embed = discord.Embed(color=0xff0000)
                        embed.set_author(
                            name=member, icon_url=member.avatar.url)
                        embed.add_field(
                            name='', value=f'Amount must be greater than 0.', inline=True)
                        await ctx.send(embed=embed)
                    else:

                        if check_acc(member) == True:
                            balance_take(ctx.author, 'wallet', amount)
                            balance_give(ctx.author, 'bank', amount)
                            embed = discord.Embed(color=0xff0000)
                            embed.set_author(
                                name=member, icon_url=member.avatar.url)
                            embed.add_field(
                                name='', value=f'{CURRENCY} {amount} deposited to bank.', inline=True)
                            await ctx.send(embed=embed)

                except:
                    traceback.print_stack()

            else:
                print('False')
                if member == ctx.author:
                    embed = discord.Embed(color=COLOUR['Bank'])
                    embed.add_field(
                        name='', value=f'You do not have a bank account. Please open an account with `!open_account`', inline=True)
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(color=COLOUR['Bank'])
                    embed.add_field(
                        name='', value=f'**{member}** does not have a bank account. Please open an account with `!open_account`', inline=True)
                    await ctx.send(embed=embed)

        except:
            traceback.print_stack()

    @commands.command(aliases=['w'])
    async def widthdraw(self, ctx, amount):
        balance_give(ctx.author, 'bank', amount)
        balance_take(ctx.author, 'wallet', amount)

        embed = discord.Embed(color=0xff0000)
        embed.set_author(name=member, icon_url=member.avatar.url)
        embed.add_field(
            name='', value=f'{CURRENCY} {amount} widthdrawn bank.', inline=True)
        await ctx.send(embed=embed)

    @commands.command(aliases=['cash'])
    async def wallet(self, ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author

        print(memdata)
        try:
            if await check_acc(ctx, member) == True:
                wallet = memdata[str(member.id)]['wallet']

                if member == ctx.author:
                    try:
                        embed = discord.Embed(color=COLOUR['Bank'])
                        embed.set_author(
                            name=member, icon_url=member.avatar.url)
                        embed.add_field(
                            name='', value=f'You have {CURRENCY} {wallet} in your wallet.', inline=True)
                        await ctx.send(embed=embed)
                    except:
                        traceback.print_stack()
                else:

                    embed = discord.Embed(color=COLOUR['Bank'])
                    embed.set_author(name=member, icon_url=member.avatar.url)
                    embed.add_field(
                        name='', value=f'{member} has {CURRENCY} {wallet} in their wallet', inline=True)
                    await ctx.send(embed=embed)

            else:
                await no_acc(ctx)
        except:
            traceback.print_stack()

    @commands.command(aliases=['bal'])
    async def balance(self, ctx):

        if await check_acc(ctx, ctx.author) == True:
            print(memdata)
            wallet = memdata[str(ctx.author.id)]['wallet']
            bank = memdata[str(ctx.author.id)]['bank']

            print(wallet)
            print(bank)

            embed = discord.Embed(title='Balance', color=COLOUR['Bank'])
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
            embed.add_field(
                name='Wallet', value=f'{CURRENCY} {wallet}', inline=True)
            embed.add_field(
                name='Bank', value=f'{CURRENCY} {bank}', inline=True)
            await ctx.author.send(embed=embed)

            if isinstance(ctx.channel, discord.channel.DMChannel) == False:
                embed = discord.Embed(color=COLOUR['Bank'])
                embed.add_field(
                    name='', value=f'Balance sent to DM.', inline=True)
                await ctx.send(embed=embed)

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


'''
BOT ACTIONS

sender command
confirmation embed
remove balance from sender
edit embed: sent

save file
send embed notif to sender
    
send embedded DM with react and amount to reciever
add balance to receiver
send embedded DM

'''
