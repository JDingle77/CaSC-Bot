# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:08:50 2021

@author: sammy
"""
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready.')
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping is {round(client.latency * 1000)}ms')

@client.command()
async def image(ctx):
    await ctx.send(file=discord.File('Connect4Board.png'))

client.run('ODA3NDcyNTI2MjE3MDUyMTYw.YB4fZA.qof50jXFk1kKTyOnlEIaIIAJ8MI')
