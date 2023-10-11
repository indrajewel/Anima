import discord
from discord.ext import commands
import config
from config import COLOUR

from func import MEMDATA, BADWORDS, SPAM
from func import memdata
from func import load_file, savememdata
from random import randint


'''
member = ctx.author
avatar = member.avatar.url
cogname = ctx.cog.qualified_name
colour = config.embed_colour[str(cogname)]
'''
badwords = load_file(BADWORDS)

cc_message = ['Suspect is drone, vehicles, or other hardened targets that poses a threat. Without the Crime Coefficient, a Threat Status is given (such as A+) and the Dominator will automatically switch to Destroy Decomposer.',
              'Suspect is not a target for enforcement action. The trigger of the Dominator will be locked.',
              'Suspect is classified as a latent criminal and is a target for enforcement action. The Dominator is set to Non-Lethal Paralyzer mode. Suspect under fire will be stunned into a stunned state of immobility and, oftentimes, a lack of consciousness.',
              'Suspect poses a serious threat to the society. Lethal force is authorized. The Dominator will automatically switch to Lethal Eliminator. Suspect that is hit by Lethal Eliminator will bloat and explode.',
              'Suspect is drone, vehicles, or other hardened targets that poses a threat. Without the Crime Coefficient, a Threat Status is given (such as A+) and the Dominator will automatically switch to Destroy Decomposer.']


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
            memdata[str(author.id)] = {'name': str(author), 'crime_coeff': 0}
            print(f'added {author} ({author.id}) to memdata')
            savememdata()

        # ignore commands
        if msg.startswith(config.PREFIX):
            return

        # cuss check
        count = 0
        score = 0
        words = []
        oldcc = memdata[str(author.id)]['crime_coeff']

        for idx in badwords:
            if idx in msg:
                count += 1
                words.append(idx)
                x = randint(5, 15)
                score += x
                newcc = oldcc+score
                memdata[str(author.id)]['crime_coeff'] = newcc

        if count > 0:
            print(f'trigger: {words}')
            print(f'{message.author} {oldcc} + {score}, new {newcc}')
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

        embed = discord.Embed(
            title=f'Crime Coefficient: {cc}', color=COLOUR['Fun'])
        embed.set_author(name=member, icon_url=avatar)
        embed.add_field(name='', value=cc_message[level], inline=False)
        await ctx.send(embed=embed)
        pass

    @commands.command()
    async def reset(self, ctx):
        print('oldmemdata:', memdata)
        for idx in memdata:
            if not idx == '1155922109936185464':
                memdata[idx]['crime_coeff'] = 0
        await ctx.send('Crime Coefficient reset to 0.')
        print('Newmemdata:', memdata)

        # update members.json
        savememdata()


async def setup(client):
    await client.add_cog(Psychopass(client))
