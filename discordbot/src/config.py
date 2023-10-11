PREFIX = '!'

COLOUR = {'Psychopass': 0x9c2b73,
          'Bank': 0x009f65,
          'Fun': 0x00eeff,
          'Fail': 0xff0000,
          'System': 0x6a329f
          }

CURRENCY = ':mushroom:'

'''
moonbowels !bal_take 1 <@435615739274330154>
traceback.print_stack()

if member == None:
    member = ctx.author


# Member does not have a bank account

if check_acc(member) == True:

    # CODE
        
        
## CHECK IF NO MEMBER PARAM ##
if member == None:
        member = ctx.author

## NO ACCOUNT EMBED ###

if member == ctx.author:
    embed=discord.Embed(color=0xff0000)
        embed.add_field(name='No bank account found', value=f'You do not have a bank account. Please open an account with ``!open_account``', inline=True)
        await ctx.send(embed=embed)

else:
    embed=discord.Embed(color=0xff0000)
    embed.add_field(name='No bank account found', value=f'{member} does not have a bank account. Please open an account with ``!open_account``', inline=True)
    await ctx.send(embed=embed)
    
    
## DATA CORROPUTED ##

embed=discord.Embed(color=0xff0000)
embed.add_field(name='Data Corrupted', value=f'Please notify bot owner.', inline=True)
await ctx.send(embed=embed)
        
        
        
'''
