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


## DEBUG ##
traceback.print_stack()

if member == None:
    member = ctx.author


## TRANSACTION ALGORITHM ##
- parameters ctx, author, amount, member

{
- load file
balance = memdata[str(member.id)]['account']

- check if account exists check_acc(ctx, member)
    if a and b in data
    elif not a and not b in data
    else
    
- check if amount > 0 check_pos(ctx, amount)
- check if amount < account balance

- check amount valid_amount(ctx, author, account, amount)
    if amount > 0
        if amount > account balance
        
        else
            perform operation   
    else:
        await embed
            

- perform operation
    - bal_give
    - bal_take
    
- save data
- async await embed
    - author
    - member

## CASES ##
- sender does not have account
- recipient does not have account
- amount is < 0
- 0 < amount < balance ###
- balance < amount

## CHECK IF NO MEMBER PARAM ##
if member == None:
        member = ctx.author

# CHECK ACCOUNT
if check_acc(member) == True:

    # CODE
        
        


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
