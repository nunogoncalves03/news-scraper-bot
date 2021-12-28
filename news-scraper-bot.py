import discord
import os
import requests
from bs4 import BeautifulSoup
from discord.ext import tasks
from keep_alive import keep_alive
import datetime

error_counter = 0


def write_all_rl_news():
    html_text = requests.get('https://www.rodoviariadelisboa.pt/comunicados').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('a', class_='titulo')
    news_file = open('rl_news.txt', 'w')
    news_list = []
    for post in posts:
        post_ref = 'https://www.rodoviariadelisboa.pt/' + post['href']
        news_list += [post_ref + '\n']
    news_file.writelines(news_list)
    news_file.close()
    print('write_all_rl_news() ✅')


def find_rl_news():
  try:
    html_text = requests.get('https://www.rodoviariadelisboa.pt/comunicados').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('a', class_='titulo')
    news_file = open('rl_news.txt', 'r')
    news_file_content = news_file.read()
    news_file.close()
    additional_news = []
    for post in posts:
        post_title = post.text.strip()
        post_ref = 'https://www.rodoviariadelisboa.pt/' + post['href']
        if post_ref not in news_file_content:
            print(f'{post_title}\n{post_ref}')
            print()
            additional_news += [[post_title, post_ref, 'Rodoviária de Lisboa', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTahAXa13o9NTAFvDIQCHBi7IxO3Z6f09_35LU85S7BmWYSkSn2bZnhnX-1f-LRv-4I-rs&usqp=CAU']]
    if additional_news != []:
        news_file = open('rl_news.txt', 'a')
        for news in additional_news:
            news_file.write(news[1] + '\n')
        news_file.close()
    print('find_rl_news() ✅')
    return additional_news
  except:
    global error_counter
    error_counter += 1
    print('find_rl_news() ❌')
    return []


def write_all_c_news():
    html_text = requests.get('https://www.carris.pt/descubra/noticias/informacoes-de-servico/').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('div', class_='container widget')
    news_file = open('c_news.txt', 'w')
    news_list = []
    for post in posts:
        post_ref = post.find('div', class_='col-12 col-md-6 image-block order-md-1').a['href']
        if post_ref[0:19] == '/descubra/noticias/' or post_ref[0:6] == '/viaje':
            post_ref = 'https://www.carris.pt' + post_ref
        news_list += [post_ref + '\n']
    news_file.writelines(news_list)
    news_file.close()
    print('write_all_c_news() ✅')


def find_c_news():
  try:
    html_text = requests.get('https://www.carris.pt/descubra/noticias/informacoes-de-servico/').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('div', class_='container widget')
    news_file = open('c_news.txt', 'r')
    news_file_content = news_file.read()
    news_file.close()
    additional_news = []
    for post in posts:
        post_ref = post.find('div', class_='col-12 col-md-6 image-block order-md-1').a['href']
        if post_ref[0:19] == '/descubra/noticias/' or post_ref[0:6] == '/viaje':
            post_ref = 'https://www.carris.pt' + post_ref
        post_title = post.find('div', class_='subtitle left').text.strip()        
        if post_ref not in news_file_content:
            print(f'{post_title}\n{post_ref}')
            print()
            additional_news += [[post_title, post_ref, 'CARRIS', 'https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/46/6b/62/466b621e-74bf-3d1a-0d83-a006dd8d8010/AppIcons-1x_U007emarketing-0-4-0-0-85-220.png/230x0w.webp']]
    if additional_news != []:
        news_file = open('c_news.txt', 'a')
        for news in additional_news:
            news_file.write(news[1] + '\n')
        news_file.close()
    print('find_c_news() ✅')
    return additional_news
  except:
    global error_counter
    error_counter += 1
    print('find_c_news() ❌')
    return []


def write_all_ml_news_1():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    html_text = requests.get('https://www.metrolisboa.pt/informar-3/noticias/', headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('h2', class_='entry-title')
    news_file = open('ml_news_1.txt', 'w')
    news_list = []
    for post in posts:
        post_title = post.a.text.strip()
        post_ref = post.a['href']
        news_list += [post_ref + '\n']
    news_file.writelines(news_list)
    news_file.close()
    print('write_all_ml_news_1() ✅')


def find_ml_news_1():
  try:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    html_text = requests.get('https://www.metrolisboa.pt/informar-3/noticias/', headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('h2', class_='entry-title')
    news_file = open('ml_news_1.txt', 'r')
    news_file_content = news_file.read()
    news_file.close()
    additional_news = []
    for post in posts:
        post_title = post.a.text.strip()
        post_ref = post.a['href']
        if post_ref not in news_file_content:
            print(f'{post_title}\n{post_ref}')
            print()
            additional_news += [[post_title, post_ref, 'Metropolitano de Lisboa', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Lisbon_Metro_logo.png/1200px-Lisbon_Metro_logo.png']]
    if additional_news != []:
        news_file = open('ml_news_1.txt', 'a')
        for news in additional_news:
            news_file.write(news[1] + '\n')
        news_file.close()
    print('find_ml_news_1() ✅')
    return additional_news
  except:
    global error_counter
    error_counter += 1
    print('find_ml_news_1() ❌')
    return []


def write_all_ml_news_2():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    html_text = requests.get('https://www.metrolisboa.pt/institucional/comunicar/comunicados/', headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('h2', class_='entry-title')
    news_file = open('ml_news_2.txt', 'w')
    news_list = []
    for post in posts:
        post_ref = post.a['href']
        news_list += [post_ref + '\n']
    news_file.writelines(news_list)
    news_file.close()
    print('write_all_ml_news_2() ✅')


def find_ml_news_2():
  try:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    html_text = requests.get('https://www.metrolisboa.pt/institucional/comunicar/comunicados/', headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('h2', class_='entry-title')
    news_file = open('ml_news_2.txt', 'r')
    news_file_content = news_file.read()
    news_file.close()
    additional_news = []
    for post in posts:
        post_title = post.a.text.strip()
        post_ref = post.a['href']
        if post_ref not in news_file_content:
            print(f'{post_title}\n{post_ref}')
            print()
            additional_news += [[post_title, post_ref, 'Metropolitano de Lisboa', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Lisbon_Metro_logo.png/1200px-Lisbon_Metro_logo.png']]
    if additional_news != []:
        news_file = open('ml_news_2.txt', 'a')
        for news in additional_news:
            news_file.write(news[1] + '\n')
        news_file.close()
    print('find_ml_news_2() ✅')
    return additional_news
  except:
    global error_counter
    error_counter += 1
    print('find_ml_news_2() ❌')
    return []


def write_all_news():
    write_all_ml_news_1()
    write_all_ml_news_2()
    write_all_rl_news()
    write_all_c_news()


#write_all_news()
client = discord.Client()

@client.event
async def on_ready():
  await client.wait_until_ready()
  channel = client.get_channel(922530769883246642)
  print(":robot: I'm ready!")
  await channel.send(":robot: I'm ready! @everyone")
  find_news.start()

@tasks.loop(seconds = 3600)
async def find_news():
  channel = client.get_channel(922530769883246642)
  await channel.send(f'Searching for news...')
  list_1 = find_ml_news_1()
  list_2 = find_ml_news_2()
  list_3 = find_rl_news()
  list_4 = find_c_news()
  channel = client.get_channel(922532062513221682)
  for news in list_1 + list_2 + list_3 + list_4:
    embed = discord.Embed(title=news[0], url=news[1], color=discord.Color.blue())
    embed.set_author(name=news[2], icon_url=news[3])
    date_time = datetime.datetime.now().strftime("%d/%m/%Y • %H:%M")
    embed.set_footer(text=f'{news[2]} • {date_time}')
    await channel.send(f'Nova notícia de **{news[2]}** @everyone\n', embed=embed)
  if error_counter > 0:
    channel = client.get_channel(922530769883246642)
    await channel.send(f'Error counter: {error_counter} @everyone')
  print(f'Error counter: {error_counter}')

keep_alive()
client.run(os.environ['token'])