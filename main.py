import discord
import os
import requests
from bs4 import BeautifulSoup
from discord.ext import tasks
from keep_alive import keep_alive
import datetime
from replit import db
from news_scraper import *


client = discord.Client()


@client.event
async def on_ready():
    await client.wait_until_ready()
    channel = client.get_channel(922530769883246642)
    print("I'm ready!")  
    await channel.send("I'm ready! @everyone")
    find_news.start()


@tasks.loop(seconds = 3600)
async def find_news():
    channel = client.get_channel(922530769883246642)
    await channel.send(f'Searching for news...')
    channel = client.get_channel(922532062513221682)
    for news in find_all_news():
        if news[0] != db['last_message']:
            embed = discord.Embed(title=news[0], url=news[1], color=discord.Color.blue())
            embed.set_author(name=news[2], icon_url=news[3])
            date_time = datetime.datetime.now().strftime("%d/%m/%Y")
            embed.set_footer(text=f'News Scraper • {date_time}')
            await channel.send(f'Nova notícia de **{news[2]}** @everyone\n', embed=embed)
            db['last_message'] = news[0]
    for error in find_errors():
        channel = client.get_channel(922530769883246642)
        await channel.send(f'**{error[0]}** @everyone\n**Error:** {error[1]}')
        reset_error_list()
    channel = client.get_channel(922530769883246642)
    await channel.send('Last message: **' + db['last_message'] + '**')
    print('Last message:', db['last_message'])


keep_alive()
client.run(os.environ['token'])