import discord
from discord.ext import commands


class cog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send('test')


async def setup(client):
    await client.add_cog(cog(client))


dat = {
    'id': {
        'bank': 0
    }
}


def check(id):
    if 'wallet' and 'bank' in dat:
        print(f'''**check_acc(): {id} owns an account
        ''')
        return True
    elif 'wallet' and 'bank' not in dat:
        print(f'''**check_acc(): {id} does not own an account
        ''')
        return False
    else:
        print('**file error')


print(check('id'))
