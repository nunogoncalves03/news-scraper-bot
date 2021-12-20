import discord
import os
import requests
from bs4 import BeautifulSoup
from discord.ext import tasks
from keep_alive import keep_alive

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
            additional_news += [[post_title, post_ref]]
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
            additional_news += [[post_title, post_ref]]
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
            additional_news += [[post_title, post_ref]]
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
            additional_news += [[post_title, post_ref]]
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
  await channel.send(":robot: I'm ready!")
  find_news.start()

@tasks.loop(seconds = 600)
async def find_news():
  channel = client.get_channel(922530769883246642)
  await channel.send('Searching for news...')
  list_1 = find_ml_news_1()
  list_2 = find_ml_news_2()
  list_3 = find_rl_news()
  list_4 = find_c_news()
  channel = client.get_channel(922532062513221682)
  for news in list_1 + list_2 + list_3 + list_4:
    await channel.send('@everyone\n' + news[0] + '\n' + news[1])
  print(f'Error counter: {error_counter}')

keep_alive()
client.run(os.environ['token'])