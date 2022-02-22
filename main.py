import discord
import os
import requests
from bs4 import BeautifulSoup
from discord.ext import tasks
from keep_alive import keep_alive
import datetime
from replit import db
from news_scraper import *
from discord_components import Select, SelectOption, ComponentsBot
from discord.utils import get
from functools import reduce


intents = discord.Intents.default()
intents.members = True
bot = ComponentsBot('!', intents=intents)


async def select_role(ctx):
    await ctx.send(content='Escolhe os sites que pretendes receber notícias. <:icon:943544386367651850>', components=[Select(
                              placeholder='Escolhe aqui!',
                              min_values=1,
                              max_values=6,
                              options=[
                                  SelectOption(label='Metropolitano de Lisboa', value='Metropolitano de Lisboa', emoji='🚇'),
                                  SelectOption(label='Rodoviária de Lisboa', value='Rodoviária de Lisboa', emoji='🚌'),
                                  SelectOption(label='CARRIS', value='CARRIS', emoji='🚎'),
                                  SelectOption(label='Fertagus', value='Fertagus', emoji='🚊'),
                                  SelectOption(label='TST', value='TST', emoji='🚌'),
                                  SelectOption(label='Uniarea', value='Uniarea', emoji='📕')
                              ],
                              custom_id='SelectRole'
    )])
    while True:
        interaction = await bot.wait_for('select_option', check=lambda inter: inter.custom_id == 'SelectRole')
        values = interaction.values
        author = interaction.author
        await author.edit(roles=[])
        for value in values:
            role = get(author.guild.roles, name=value)
            await author.add_roles(role)
        try:
            await interaction.send('Vais receber notícias dos seguintes sites: ' + reduce(lambda x, y: x + ', ' + y, values) + '.')
        except:
            await ctx.send('Vais receber notícias dos seguintes sites: ' + reduce(lambda x, y: x + ', ' + y, values) + f'. <:icon:943544386367651850> {author.mention}\nIgnora a mensagem "News Scraper is thinking..."')


@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print(f'Logged in as {bot.user}!')
    select_role_channel = bot.get_channel(943484725614481430)
    logs_channel = bot.get_channel(922530769883246642)
    await logs_channel.send(f'Logged in as {bot.user}! <:icon:943544386367651850> @everyone')
    find_news.start()
    await select_role_channel.purge(limit=10)
    await select_role(select_role_channel)


@bot.event
async def on_member_join(member):
    guild = bot.get_guild(922444030720245810)
    channel = guild.get_channel(943597491167821894)
    await channel.send(f'Bem-vindo ao servidor, {member.mention}! Vai ao <#943484725614481430> para escolheres os sites que pretendes receber notícias. <:icon:943544386367651850>')


@tasks.loop(seconds = 3600)
async def find_news():
    logs_channel = bot.get_channel(922530769883246642)
    await logs_channel.send(f'Searching for news... <:icon:943544386367651850>')
    for news in find_all_news():
        if news[0] != db['last_message']:
            embed = discord.Embed(title=news[0], url=news[1], color=discord.Color.blue())
            embed.set_author(name=news[2], icon_url=news[3])
            date_time = datetime.datetime.now().strftime("%d/%m/%Y")
            embed.set_footer(text=f'News Scraper • {date_time}')
            channel = bot.get_channel(news[4])
            role = get(channel.guild.roles, name=news[2])
            await channel.send(f'Nova notícia de **{news[2]}** {role.mention}\n', embed=embed)
            db['last_message'] = news[0]
    for error in find_errors():
        await logs_channel.send(f'**{error[0]}** @everyone\n**Error:** {error[1]}')
        reset_error_list()
    await logs_channel.send('Last message: **' + db['last_message'] + '**')
    print('Last message:', db['last_message'])


@bot.event
async def on_message(message):
    if message.channel.type == discord.ChannelType.news:
        await message.publish()


keep_alive()
bot.run(os.environ['token'])