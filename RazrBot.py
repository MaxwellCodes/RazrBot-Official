import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import asyncio

client = commands.Bot(command_prefix='-')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('-hello'):
            await message.channel.send('Hi! {0.author.mention}'.format(message))
        if message.content.startswith('-info'):
            await message.channel.send('Hello, I am RazrBot. Your helpful and funny friend. I was made by RazrX.'.format(message))
        if message.content.startswith('-guessgame'):
            await message.channel.send('Guess a number between 1 and 10.'.format(message))

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send('Oops. It is actually {}.'.format(answer))
        if message.content.startswith('RazrBot'):
            await message.channel.send('That Me!'.format(message))
        if message.content.startswith('-instantregret'):
            await message.channel.send('https://www.youtube.com/playlist?list=PLv3TTBr1W_9tppikBxAE_G6qjWdBljBHJ'.format(message))

@client.command()
async def kick(ctx, member : discord.Member,*, reason=None):
    await member.kick(reason=reason)
    await message.channel.send('kicked {member} from the server'.format(message))

@client.command()
async def ban(ctx, member : discord.Member,*, reason=None):
    await member.ban(reason=reason)
    await message.channel.send('banned {member} from the server'.format(message))


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await message.channel.send('Purged {amount} messages'.format(message))
        
    



    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)       

client = MyClient()
client.run('NTk2ODQ1NDU4MTczNzIyNjI0.XR_e_A.hpPhVgQtoZP-qyHdDeeMGr_wdXk')
