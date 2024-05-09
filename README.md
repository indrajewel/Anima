# Anima
WIP Discord Bot
- File saving and loading functional
- Economy System WIP

## main.py
	
## func.py
### functions:
	load_file('file')
	savememdata()
	addmem(author)
	gen_rand(digits)

	await no_acc(ctx, member=None)
	await data_corrupt(ctx)
	await invalidmem(ctx)
	await err(ctx)
	await embedd(ctx)
	
	await check_acc(ctx, member)
	await pos(ctx, amount)
	await can_afford(ctx, member, account, amount)
	valid_amount(ctx, author, account, amount)

	balance_give(ctx, author, account, amount, member=None)
	balance_take(ctx, author, account, amount, member=None)

	memdata = load_file(MEMDATA)

## bank.py
### commands:
	open_account - Functional

	bal_award - Functional
	bal_take - Functional

	deposit - Functional
	widthdraw - Functional

	wallet - Functional
	balance - Functional

	etransfer - WIP
	drop - WIP
	awarddrop
	getcard - Functional

## fun.py
### commands
	spam - Functional
	betflip - awaiting bank and funcs
