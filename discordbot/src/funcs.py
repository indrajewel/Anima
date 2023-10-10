import discord
from discord.ext import commands
from config import COLOUR, CURRENCY

import json
import os
from random import randint

USERDATA = 'C:\\Users\\Adrian\\git\\Anima\\discordbot\\src\\data\\users.json'


class User:
    # input member as string of ID
    def __init__(self, id, name):
        self.id = id
        self.name = member
        self.crime_coeff = 0

    def ccadd(self, amount):
        pass

    def ccsub(self, amount):
        pass

    def open_bank(self):
        self.wallet = 10
        self.bank = 250
        pass

    def bank_add(self, amount):
        self.wallet += amount
        pass

    def bank_sub(self, amount):
        self.wallet -= amount
        pass


'''
async def on_message(message):
    if message.author not in memdata:
        
    
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


def saveuserdata():
    with open(USERDATA, 'w') as outf:
        json.dumps(userdata, outf, indent=4)
    print(f'**saveuserdata(): users.json overwritten')


userdata = load_file(USERDATA)
print(userdata)

# add user to members.json
'''
async def on_message(message):
    
'''


def add_user(member):
    # construct User object with ID as name
    user = User(member)
    print(user)
    # add to userdatalist
    json = json.dumps(user.__dict__)
    print(json)
    # save to json
    saveuserdata()


# add_user('userid')

user = User('moon')
print(m)
