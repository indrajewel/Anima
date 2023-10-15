import discord
from discord.ext import commands
import config
from config import COLOUR

from random import randint, uniform

from func import MEMDATA, BADWORDS, SPAM
from func import memdata
from func import load_file, savememdata

from func import check_acc, balance_give, balance_take, sufficient

'''
member = ctx.author
avatar = member.avatar.url
cogname = ctx.cog.qualified_name
colour = config.embed_colour[str(cogname)]
'''
badwords = load_file(BADWORDS)
# member = None
'''
cc_message = [f'{member} is drone, vehicles, or other hardened targets that poses a threat. Without the Crime Coefficient, a Threat Status is given (such as A+) and the Dominator will automatically switch to Destroy Decomposer.',
              f'Suspect is not a target for enforcement action. The trigger of the Dominator will be locked.',
              f'**{member}** is classified as a latent criminal and is a target for enforcement action. The Dominator is set to Non-Lethal Paralyzer mode. Suspect under fire will be stunned into a stunned state of immobility and, oftentimes, a lack of consciousness.',
              f'{member} poses a serious threat to the society. Lethal force is authorized. The Dominator will automatically switch to Lethal Eliminator. Suspect that is hit by Lethal Eliminator will bloat and explode.',
              f'{member} is drone, vehicles, or other hardened targets that poses a threat. Without the Crime Coefficient, a Threat Status is given (such as A+) and the Dominator will automatically switch to Destroy Decomposer.']
'''


def cc_level(cc):
    if cc < 100:
        level = 1
    elif cc < 299:
        level = 2
    elif cc >= 300:
        level = 3
    else:
        level = 0
    return level


def cc_message(cc):
    cc_level(cc)
    print(f'cc_embed({cc})')
    message = [f'Suspect is drone, vehicles, or other hardened targets that poses a threat. Without the Crime Coefficient, a Threat Status is given (such as A+) and the Dominator will automatically switch to Destroy Decomposer.',
               f'Suspect is not a target for enforcement action. The trigger of the Dominator will be locked.',
               f'Suspect is classified as a latent criminal and is a target for enforcement action. The Dominator is set to Non-Lethal Paralyzer mode. Suspect under fire will be stunned into a stunned state of immobility and, oftentimes, a lack of consciousness.',
               f'Suspect poses a serious threat to the society. Lethal force is authorized. The Dominator will automatically switch to Lethal Eliminator. Suspect that is hit by Lethal Eliminator will bloat and explode.']

    return message[cc_level(cc)]


def cc_add(member, coef=1, base=0):
    oldcc = memdata[str(member.id)]['crime_coeff']
    print(f'**cc_add({member}, coef: {coef}x, base: +{base}) CC = {oldcc}')

    score = round((uniform(1, 9)*coef+base), 1)
    newcc = round((oldcc+score), 1)
    memdata[str(member.id)]['crime_coeff'] = newcc
    print(f'    {member} CC increased by {score}, total {newcc}')
    return True


def cc_take(member, coef=1, base=0):
    oldcc = memdata[str(member.id)]['crime_coeff']
    print(f'**cc_take({member}, coef: {coef}x, base: +{base}) CC = {oldcc}')
    score = round((uniform(1, 9)*coef+base), 1)

    if oldcc > 0 and score <= oldcc:

        newcc = round((oldcc+score), 1)
        memdata[str(member.id)]['crime_coeff'] = newcc
        print(f'    {member} CC decreased by {score}, total {newcc}')
        return True, score

    elif score > oldcc:
        newcc = 10
        memdata[str(member.id)]['crime_coeff'] = newcc
        print(f'    {member} CC decreased by {score}, total {newcc}')
        return True

    else:
        return False
        print(f'**    CC is already 0')


def cc_rand(member, coef=1, base=0):
    print(f'cc_rand({member}, coef:{coef}x, base:+{base})')
    oldcc = memdata[str(member.id)]['crime_coeff']
    score = randint(-9, 9)*coef+base
    newcc = oldcc+score
    memdata[str(member.id)]['crime_coeff'] = newcc
    print(f'    {member} CC fluctuated by {score}, total {newcc}')
    return score


async def cc_embed(ctx, member, delta, add):

    pass


class Psychopass(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        msg = message.content
        author = message.author

        # check if in memdata
        if str(author.id) not in memdata:
            # updates memdata
            cc = round(uniform(15, 25), 1)
            memdata[str(author.id)] = {'name': str(author), 'crime_coeff': cc}
            print(
                f'added {author} ({author.id}) to memdata with crime_coeff {cc}')
            savememdata()

        # ignore commands
        if msg.startswith(config.PREFIX):
            return

        # cuss check
        count = 0
        words = []

        for idx in badwords:
            if idx in msg:
                count += 1
                words.append(idx)

                cc_add(author, coef=0.5)

        if count > 0:
            print(f'trigger: {words}')
            savememdata()

    @commands.command()
    async def psychopass(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        avatar = member.avatar.url
        memdata = load_file(MEMDATA)

        if str(ctx.author.id) not in memdata:
            await ctx.send(f'{member} cannot be evaluated.')
            return

        cc = memdata[str(member.id)]['crime_coeff']

        if cc < 100:
            level = 1
        elif cc < 299:
            level = 2
        elif cc >= 300:
            level = 3
        else:
            level = 0

        try:
            embed = discord.Embed(
                title=f'PSYCHO-PASS', color=COLOUR['Fun'])
            embed.set_author(
                name=f'''name: {member}
id: {member.id}''', icon_url=member.avatar.url)
            embed.set_thumbnail(url=member.avatar.url)
            embed.add_field(
                name=f'Crime Coefficient: {cc}', value=cc_message(cc), inline=False)
            await ctx.send(embed=embed)

        except Exception as e:
            print(e)
            traceback.print_stack()

    @commands.command(aliases=['forgive'])
    @commands.is_owner()
    async def pardon(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        print('oldmemdata:', memdata)

        memdata[str(member.id)]['crime_coeff'] = 0

        embed = discord.Embed()
        embed.set_author(name=member, icon_url=member.avatar.url)
        embed.add_field(
            name='', value='Crime Coefficient reset to 0', inline=False)
        await ctx.send(embed=embed)
        print('Newmemdata:', memdata)

        # update members.json
        savememdata()

    @commands.command('ssreset')
    @commands.is_owner()
    async def pardonall(self, ctx, member: discord.Member = None):
        print('oldmemdata:', memdata)
        for idx in memdata:
            if not idx == '1155922109936185464':
                memdata[idx]['crime_coeff'] = 0
        embed = discord.Embed()
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
        embed.add_field(name='Sybil System Reset',
                        value='All Crime Coefficients reset to 0', inline=False)
        await ctx.send(embed=embed)

        print('Newmemdata:', memdata)

        # update members.json
        savememdata()

    @commands.command()
    async def pray(self, ctx):
        if cc_take(ctx.author) == True:
            savememdata()

    @commands.command()
    async def bribe(self, ctx, amount=50):
        try:
            if await check_acc(ctx, ctx.author, embed=True) and \
                    await sufficient(ctx, 'wallet', amount) == True and \
                    balance_take(ctx, ctx.author, 'wallet', amount) == True and \
                    bool(cc_take(ctx.author, base=amount//2)) == True:
                savememdata()

        except Exception as e:
            print(e)
            traceback.print_stack()


async def setup(client):
    await client.add_cog(Psychopass(client))
