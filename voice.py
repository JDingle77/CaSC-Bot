# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:08:50 2021

@authors: Sammy, James, Joshua, Nathan
"""
#basic stuff
import random
import discord
from discord.ext import commands

#text to speech
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/e432d9e8-d8a4-4c16-b7d5-26ce1a966ffc'
apikey = 'gR3aw12wJ2-nIdN_PigaacXsZvH4koSfRp2ukorv6Vxb'
authenticator = IAMAuthenticator(apikey)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)
text_to_speech.set_service_url(url)

#prefix
client = commands.Bot(command_prefix = '!')
@client.command()
async def on_ready():
    print('Bot is ready.')
    await client.change_presence(activity=discord.Game("!info for introduction!"))
    
@client.command()
async def info(ctx):
    embed=discord.Embed(title="HI!", url="https://www.youtube.com/watch?v=KxGRhd_iWuE", description="I'm CaSC, the Connections-and-Self-Care discord bot!\nI have two main functions, motivation and connect 4!", color=0xFF5733)
    embed.set_thumbnail(url="https://i.ytimg.com/vi/kDY1y0OL50A/hqdefault.jpg")
    await ctx.send(embed=embed)
    
    embed=discord.Embed(title="Motivation!", url="https://www.youtube.com/watch?app=desktop&v=kGOQfLFzJj8", description="I can send and read you motivational messages! You can do it!", color=0xB3DB20)
    embed.set_thumbnail(url="https://i.ytimg.com/vi/kGOQfLFzJj8/hqdefault.jpg")
    embed.add_field(name="!join", value="I'll join the voice channel you are currently in! The more the merrier!", inline=False)
    embed.add_field(name="!motivate",value="I'll send and read you a motivational quote! But I can only read it outloud if I'm in the voice call with you :)", inline=False)
    embed.add_field(name="!leave", value="Once you're motivated enough, I'll leave and let you do great things in life!")
    await ctx.send(embed=embed)
    
    embed=discord.Embed(title="Connect4!", url="https://www.youtube.com/watch?v=KN3nohBw_CE",description="With me, you can play connect 4 with your favorite discord buddies!\nHere are the commands:", color=discord.Color.blue())
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/659562869041659919/807889690920615936/connect4.png")
    embed.add_field(name="!connect4", value="Starts the game of connect 4! An empty connect 4 board will appear and players can drop in pucks by typing the numbers 0-6!", inline=False)
    embed.add_field(name="!quit",value="Quits the game and resets the board!.", inline=False)
    embed.add_field(name="IMPORTANT NOTE:", value="Cannot use non-connect4 functions while in a game of connect 4.")
    await ctx.send(embed=embed)
    
    
@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)
    await ctx.send('Hiii!')
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.send('See you later!')
    await ctx.voice_client.disconnect()
    
@client.command() #I had to use: conda install -c conda-forge ffmpeg
async def motivate(ctx):
    messages = ["Ur Hot!", "JUST KEEP SWIMMING", "Honestly you are so hot", "LETS GO", "YOU are a WINNER!", "Keep it up dude","You can make it to Gold!", "It's okay everyone ints sometimes", "It's okay to be down bad", "You are so POGU", "You are my FRIEND!", "YESSIR", "LET'S GO BOYS", "ITS NOW OR NEVER", "DON'T QUIT", "WHEN THE GOING GETS TOUGH, THE TOUGH GET GOING", "Keep pushing bro", "You may be sad now, but the brightness I see in your future is making me legally blind", "Everyday we must love, laugh, and learn","It's fine to not be okay","Love yourself, you're pog!", "Yo princess keep your head up, your tiara is falling", "Quarantine is hard I know, but giving up is worse", "If you back down now, you'll set a precedent of giving up. DO NOT QUIT", "It's TIME TO GO POGCHAMP STUDY GRIND LETS GO", "I love you", "Love others and love yourself", "Rest and relaxation is just as important as getting good grades", "I've told you this already but you are just so hot", "Be confident in who you are", "There are people in this world that look up to you", "We all have been through painful experiences, our job is to uplift others out of their own", "If you set 10 minutes of time to dedicate to one thing what would it be?", "Physical health can translate to your studies. Make sure to sleep, eat, and exercise!", "You are a creative, profoundly smart, and deep individual", "Can you really say that you are not awesome", "Be like Aang, save the world!", "DAB right now, BET", "On the count of three let out the biggest scream 1.... 2.... 3!", "Ready or not HERE YOU COME", "Joshua Zhang once said you are dope", "Can you move it move it?", "What's up? The Sky!", "No printer just fax you are hot", "Can I get a HOOOOOOOYAAAA?", "Live everyday like your last", "Stop complaining and do it", "You are strong, you are the great King Kong", "Hello nice to meet you, my name is GO AND DO YOUR STUDYING", "Anyone like pie? Cause I circlently do", "I used to be a fan of you, but now I'm an airconditioner" ,"If you are a simp, simping is for the strong", "IM A SIMP FOR YOU!", "Go to sleep tonight know that someone out there in the world is simping for you", "Do you know da wae?", "Health is true wealth", "WE GO UP", "Fist bump? 3 2 1 BOOOSH!", "Any pogchampers?", "Make a list of things to do and prioritize your tasks based on two things: improtance and time due. Do the most important and close tasks first!", "Chill, watch an anime! I reccomend Hunter x Hunter, Promised Neverland, and Attack on Titan!", "Every person is quirky in there on ways", "Being different is awesome!", "I've told you this three times before but I can't stop thinking about how hot you are", "Drink 50oz of water everyday!", "Eat on time, sleep early, and make sure to have some time to yourself", "Who is someone in your life that has impacted you? DM your appreciation right now and make a connection again!", "If you have ever been on a roller coaster, you know life has its up and its downs", "Is it hot in here cause your so lit!", "Call someone right now and say you love them", "Don't just call people for when you need something. Set up a time to catch up with your friends!", "Family is important, make sure to let your family know how much you love them!", "Do things your passionate about!", "If you look at every successful person in the world, they did not do it for money, they did it because they had a genuine interest. BE passionate about something and pursue it!"] 
    sent = ""; 
    sent = random.choice(messages)
    await ctx.send(sent)
    
    with open('./speech.mp3', 'wb') as audio_file:
        res = text_to_speech.synthesize(sent, accept='audio/mp3', voice ='en-US_AllisonV3Voice').get_result()
        audio_file.write(res.content)
    ctx.voice_client.play(discord.FFmpegPCMAudio('speech.mp3'), after=lambda e: print('speech finished'))
    ctx.voice_client.source = discord.PCMVolumeTransformer(ctx.voice.source, 0.03)


client.run('token')
