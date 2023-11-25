import discord
from discord.ext import commands
import traceback


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def get_avatar(self, ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author
        avatar = member.avatar.url

        embed = discord.Embed(
            title=f"{member}'s avatar", url=member.avatar.url)
        embed.set_image(url=avatar)
        await ctx.send(embed=embed)
        print(avatar)


try:
    async def setup(client):
        await client.add_cog(Utility(client))
except Exception as e:
    print(e)
    traceback.print_stack()
