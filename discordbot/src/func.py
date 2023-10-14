import discord
from discord.ext import commands
from config import COLOUR, CURRENCY, BOT_OWNER

import json
import os
from random import randint
import traceback

MEMDATA = 'C:\\Users\\Adrian\\git\\Anima\\discordbot\\src\\data\\members.json'
BADWORDS = 'C:\\Users\\Adrian\\git\\Anima\\discordbot\\src\\data\\badwords.txt'
SPAM = 'C:\\Users\\Adrian\\git\\Anima\\discordbot\\src\\data\\spamlist.txt'

'''
MEMDATA = f'{os.getcwd()}\data\members.json'
BADWORDS = f'{os.getcwd()}\data\\badwords.txt'
SPAM = f'{os.getcwd()}\data\spamlist.txt'

print(MEMDATA)
print(BADWORDS)
print(SPAM)
'''


def load_file(file_dir):
    if '.json' in file_dir:
        with open(file_dir, 'r') as infile:
            data = json.load(infile)

    elif '.txt' in file_dir:
        with open(file_dir, 'r') as infile:
            list1 = infile.readlines()
            data = [x.replace('\n', '') for x in list1]

    print(f'*Opened: {file_dir[46:60]} | {data}')
    return data

## SAVE DATA ##


def savememdata():
    with open(MEMDATA, 'w') as outf:
        json.dump(memdata, outf, indent=4)
    print(f'''*savememdata(): members.json overwritten
    ''')


def addmem(author):
    memdata[str(author.id)] = {'name': str(author), 'crime_coeff': 0}
    print(f'*Added <{author}> <{author.id}> to memdata')


def updatekey(author, key, data):
    memdata[str(author.id)][key] = data
    print(f'*Updated memdata: {author} ({author.id}: {key}:{data})')

## GENERATE N RANDOM DIGITS ##


def gen_rand(digits):
    string = ''.join(str(randint(0, 9)) for item in range(digits))
    return string


## SEND EMBED: NO BANK ACCOUNT FOUND ##


async def no_acc(ctx, member: discord.Member=None):
    print(member)
    if member == None:
        member = ctx.author

    if member == ctx.author:
        embed = discord.Embed(color=COLOUR['Fail'])
        embed.add_field(name='No bank account found',
                        value=f'You do not have a bank account. Please open an account with ``!open_account``', inline=True)
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(color=COLOUR['Fail'])
        embed.add_field(name='No bank account found',
                        value=f'**{member}** does not have a bank account. Please open an account with ``!open_account``', inline=True)
        await ctx.send(embed=embed)

## SEND EMBED: DATA CORRUPTED ##


async def data_corrupt(ctx):
    embed = discord.Embed(color=COLOUR['Fail'])
    embed.add_field(name=':no_entry: Data Corrupted',
                    value=f'Please reset with ``!open_account`` and/or notify bot owner <@435615739274330154>.', inline=True)
    await ctx.send(embed=embed)

## SEND EMBED: UNKNOWN ERROR ##


async def err(ctx):
    embed = discord.Embed(color=COLOUR['Fail'])
    embed.add_field(name=':no_entry: Unknown Error',
                    value=f'Please notify bot owner {BOT_OWNER}!', inline=True)
    await ctx.send(embed=embed)

## SEND EMBED: INVALID MEMBER ##


async def invalidmem(ctx):
    embed = discord.Embed(color=COLOUR['Fail'])
    embed.add_field(name='Invalid Input',
                    value='Missing parameter: member', inline=False)
    await ctx.send(embed=embed)


async def embed_d(ctx, member, account, amount):
    print('*embed_d')

    embed = discord.Embed(color=COLOUR['Bank'])
    embed.set_author(name=member, icon_url=member.avatar.url)

    if account == 'wallet':
        embed.add_field(
            name='Funds Added', value=f"Deposited  {CURRENCY} {amount} to {member}'s wallet.", inline=True)
    elif account == 'bank':
        embed.add_field(
            name='Funds Added', value=f"Deposited  {CURRENCY} {amount} to {member}'s bank account.", inline=True)

    await ctx.send(embed=embed)


async def embed_w(ctx, member, account, amount):

    embed = discord.Embed(color=COLOUR['Bank'])
    embed.set_author(name=member, icon_url=member.avatar.url)

    if account == 'wallet':
        embed.add_field(
            name='Funds Removed', value=f"Widthdrew  {CURRENCY} {amount} from {member}'s wallet.", inline=True)
    elif account == 'bank':
        embed.add_field(
            name='Funds Removed', value=f"Widthdrew  {CURRENCY} {amount} from {member}'s bank account.", inline=True)

    await ctx.send(embed=embed)

## CHECK VALUE: IF USER HAS ACCOUNT ##


async def check_acc(ctx, member):
    print(f'**check_acc({member}) id:{member.id}')
    try:
        if 'wallet' in memdata[str(member.id)] and 'bank' in memdata[str(member.id)]:
            print(f'''**check_acc({member}): True - owns an account
            ''')
            return True

        elif 'wallet' not in memdata[str(member.id)] and 'bank' not in memdata[str(member.id)]:
            print(f'''**check_acc({member}): False - does not own an account
            ''')

            await no_acc(ctx, member)
            return False
    except:
        print(f'''**check_acc({member}): Error at memdata[{member.id}]
            ''')
        await data_corrupt(ctx)
        traceback.print_stack()


async def pos(ctx, amount):
    print(f'pos({amount})')
    if int(amount) > 0:
        print(f'    pos(): True - is positive integer')
        return True
    else:
        print(f'    pos(): False - is not positive integer')
        embed = discord.Embed(color=COLOUR['Fail'])
        embed.add_field(name='Invalid amount.',
                        value='Amount must be greater than 0.', inline=True)
        await ctx.send(embed=embed)
        return False


async def can_afford(ctx, account, amount):
    print(f'***can_afford({ctx.author}, {account}, {amount})')
    if int(amount) > memdata[str(ctx.author.id)][str(account)]:
        embed = discord.Embed(color=COLOUR['Fail'])
        embed.add_field(name='Insufficient Funds',
                        value=f'Not enough {CURRENCY} in {account}!', inline=False)
        await ctx.send(embed=embed)
        print(f'    can_afford({ctx.author}, {account}, {amount}): False')
        return False

    else:
        print(f'    can_afford({ctx.author}, {account}, {amount}): True')
        return True


async def sufficient(ctx, account, amount):
    print(f'***sufficient({account}, {amount})')
    if await pos(ctx, amount) == True and \
            await can_afford(ctx, account, amount) == True:
        return True

    else:
        return False


def balance_give(ctx, member, account, amount):
    print(f'***balance_give({member}, {account}, {amount})')
    try:
        memdata[str(member.id)][str(account)] += amount
        newbal = memdata[str(member.id)][str(account)]
        print(
            f'    ***balance_give({member}, {account}, {amount}) Total: {newbal}')
        return True

    except:
        print('***balance_give(): Error; check params, check_acc(), pos()')


def balance_take(ctx, member, account, amount):
    print(f'***balance_take({member}, {account}, {amount})')
    try:
        memdata[str(member.id)][str(account)] -= amount
        newbal = memdata[str(member.id)][str(account)]
        print(
            f'    ***balance_take({member}, {account}, {amount}) Total: {newbal}')
        return True

    except:
        print('***balance_take(): Error; check params, check_acc(), pos()')


memdata = load_file(MEMDATA)

'''
items = open(SPAMFILE, 'w')

for idx in spamlist:
    items.write(idx+"\n")
items.close()

items = open(SPAMFILE, 'r')
itemlist = items.readlines()
print(itemlist)
items.close()
'''

'''
spamlist = ['hop on duck', 'i miss u uwu', 'lets play',
            'hop on', 'i need your yummy cummy wummy in my tummy honey', 'gaems',
            'there is a distinct lack of your girthy cock in my butthole',
            'i find your lack of presence disturbing', 'please', 'i am begging u',
            'games???', 'lets playyy', 'hop on vc', 'vc party'
            ]

altbadwords = ['ass', 'shit', 'fuck']
'''
