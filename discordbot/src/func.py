import discord
from discord.ext import commands
from config import COLOUR, CURRENCY

import json
import os
from random import randint

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

    print(f'**Opened: {file_dir[46:60]} | {data}')
    return data


def savememdata():
    with open(MEMDATA, 'w') as outf:
        json.dump(memdata, outf, indent=4)
    print(f'**savememdata(): members.json overwritten')


def addmem(author):
    memdata[str(author.id)] = {'name': str(author), 'crime_coeff': 0}
    print(f'**Added <{author}> <{author.id}> to memdata')


def updatekey(author, key, data):
    memdata[str(author.id)][key] = data
    print(f'**Updated memdata: {author} ({author.id}: {key}:{data})')


async def throw_err():
    pass


def gen_rand(digits):
    string = ''.join(str(randint(0, 9)) for item in range(digits))
    return string


def check_acc(member):
    memdata = load_file(MEMDATA)
    print(member.id)

    if 'wallet' in memdata[str(member.id)] and 'bank' in memdata[str(member.id)]:
        print(f'''**check_acc(): True: {member} owns an account
        ''')
        return True
    elif 'wallet' not in memdata[str(member.id)] and 'bank' not in memdata[str(member.id)]:
        print(f'''**check_acc(): {member} does not own an account
        ''')
        return False
    else:
        print(f'''**check_acc(): Error at memdata[{member.id}] ({member})
        ''')
        raise Excepion('file corrupted')


async def balance_give(member, account, amount, ctx):
    try:
        oldbal = memdata[str(member.id)][str(account)]
        amount = int(amount)
        print(f"**memdata['{member.id}'][{account}] {member} OldBal: {oldbal}")
    except:
        embed = discord.Embed(title='Balance Deposit Failed',
                              color=COLOUR["Fail"])
        embed.set_author(name=member, icon_url=member.avatar.url)
        embed.add_field(
            name='', value=f'{member} does not own a bank account.', inline=True)
        await ctx.send(embed=embed)
        print(f'{member} does not have bank account')

    if amount > 0:
        try:
            memdata[str(member.id)][str(account)] += amount
            newbal = memdata[str(member.id)][str(account)]

            print(
                f"**balance_give(): memdata[{member}][{account}] {member} NewBal: {newbal}")

            embed = discord.Embed(title='Funds Added', color=COLOUR['Bank'])
            embed.set_author(name=member, icon_url=member.avatar.url)
            embed.add_field(
                name='', value=f"Deposited  {CURRENCY} {amount} to {member}'s bank account.", inline=True)
            await ctx.send(embed=embed)

        except:
            embed = discord.Embed(
                title='Balance Deposit Failed', color=0xff0000)
            embed.set_author(name=member, icon_url=member.avatar.url)
            embed.add_field(
                name='', value='Unknown error. Please try again later', inline=True)
            await ctx.send(embed=embed)
            print(f'failed to update {member} {account}')

    else:
        embed = discord.Embed(
            title='Balance Update Failed', color=COLOUR['Fail'])
        embed.set_author(name=member, icon_url=member.avatar.url)
        embed.add_field(
            name='', value='Amount must be greater than 0.', inline=True)
        await ctx.send(embed=embed)
        print("**Invalid amount. Must be greater than 0")


async def balance_take(member, account, amount, ctx):
    try:
        oldbal = memdata[str(member.id)][str(account)]
        amount = int(amount)
        print(f"**memdata['{member.id}'][{account}] {member} OldBal: {oldbal}")
    except:
        embed = discord.Embed(title='Balance Update Failed',
                              color=COLOUR["Fail"])
        embed.set_author(name=member, icon_url=member.avatar.url)
        embed.add_field(
            name='', value=f'{member} does not own a bank account.', inline=True)
        await ctx.send(embed=embed)
        print(f'{member} does not have bank account')

    if amount > 0:
        try:
            memdata[str(member.id)][str(account)] += amount
            newbal = memdata[str(member.id)][str(account)]

            print(
                f"**balance_give(): memdata[{member}][{account}] {member} NewBal: {newbal}")

            embed = discord.Embed(title='Funds Removed', color=COLOUR['Bank'])
            embed.set_author(name=member, icon_url=member.avatar.url)
            embed.add_field(
                name='', value=f"Widthdrew  {CURRENCY} {amount} from {member}'s bank account.", inline=True)
            await ctx.send(embed=embed)

        except:
            embed = discord.Embed(
                title='Balance Update Failed', color=0xff0000)
            embed.set_author(name=member, icon_url=member.avatar.url)
            embed.add_field(
                name='', value='Unknown error. Please try again later', inline=True)
            await ctx.send(embed=embed)
            print(f'failed to update {member} {account}')

    else:
        embed = discord.Embed(
            title='Balance Update Failed', color=COLOUR['Fail'])
        embed.set_author(name=member, icon_url=member.avatar.url)
        embed.add_field(
            name='', value='Amount must be greater than 0.', inline=True)
        await ctx.send(embed=embed)
        print("**Invalid amount. Must be greater than 0")


memdata = load_file(MEMDATA)
badwords = load_file(BADWORDS)
spamlist = load_file(SPAM)

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
