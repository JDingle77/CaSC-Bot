# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:08:50 2021

@author: nathan
"""
import asyncio
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready.')
    
@client.command()
async def joinvc(ctx, *, channel: discord.VoiceChannel):
    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)
    await ctx.send('Hiii!')
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.send('See you later!')
    await ctx.voice_client.disconnect()

client.run('ODA3NDcyNTI2MjE3MDUyMTYw.YB4fZA.qof50jXFk1kKTyOnlEIaIIAJ8MI')
