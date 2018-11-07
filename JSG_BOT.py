import discord
from discord.ext import commands
import random
import traceback
import time
import asyncio
import datetime
description = 'A bot for the JSG guild.'
bot = commands.Bot(command_prefix='!', description=description)

token = 'NTAzOTA3MDYwMTc0NDIyMDE2.Dq9UqQ.i0a_YXMxTkQmcAd5iNfp3ZZsXWc'



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def avatar(ctx, server, realm):
    await ctx.channel.purge(limit=1)
    server = server.upper()
    realm = realm.capitalize()
    if ctx.channel.name == 'avatar-callout':
        message = await ctx.send("@deleted-role\nAvatar in {} {}\nCalled by: {}".format(server, realm, ctx.author.mention))
        await message.add_reaction('💀')
        await message.add_reaction('❤')
        reaction = await bot.wait_for('reaction_add', check=lambda reaction_i, user: (reaction_i.emoji == '💀' or reaction_i.emoji == '❤') and not(bot.user == user))
        print(str(reaction[0]))
        if str(reaction[0]) == '💀':
            await message.delete()
        elif str(reaction[0]) == '❤':
            await message.clear_reactions()
            await message.edit(content='Avatar died and shatters have been dropped in ' + server + " "  + realm + ". 30 Seconds remaining.")
            await asyncio.sleep(30)
            await message.delete()
    else:
        await ctx.send("Channel must be called 'avatar-callout'")


@bot.command()
async def delete(ctx, amount: int):
    role = discord.utils.get(ctx.guild.roles, name="Leader")
    if role in ctx.author.roles:
        if amount > 150:
            await ctx.send("Too many messages... Must be under 150.")
        else:
            await ctx.channel.purge(limit=amount+1)
    else:
        message = await ctx.send("You're not a leader.")
        await asyncio.sleep(2)
        await message.delete()


@bot.command()
async def role(ctx):
    await ctx.channel.purge(limit=1)
    roles = discord.utils.get(ctx.guild.roles, name="Tablet Crew")
    user = ctx.message.author
    if roles not in ctx.author.roles:
        await user.add_roles(roles)
    else:
        await user.remove_roles(roles)


bot.run(token)