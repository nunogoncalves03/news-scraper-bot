import requests
from bs4 import BeautifulSoup
from replit import db
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


error_list = []


def find_rl_news():
  try:
    html_text = requests.get('https://www.rodoviariadelisboa.pt/comunicados').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('a', class_='titulo')
    additional_news = []
    for post in posts:
        post_title = post.text.strip()
        post_ref = 'https://www.rodoviariadelisboa.pt/' + post['href']
        if post_ref not in db.keys():
            print(f'{post_title}\n{post_ref}')
            print()
            additional_news += [[post_title, post_ref, 'Rodoviária de Lisboa', 'https://i.ibb.co/848PYh9/rl.png', 943596787476877336]]
    if additional_news != []:
        for news in additional_news:
            db[news[1]] = ''
    print('find_rl_news() ✅')
    return additional_news
  except Exception as error:
    global error_list
    if ['find_rl_news() ❌', error] not in error_list:
        error_list = error_list + [['find_rl_news() ❌', error]]
    print('find_rl_news() ❌')
    return []


def find_c_news():
  try:
    html_text = requests.get('https://www.carris.pt/descubra/noticias/informacoes-de-servico/').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('div', class_='container widget')
    additional_news = []
    for post in posts:
        post_ref = post.find('div', class_='col-12 col-md-6 image-block order-md-1').a['href']
        if post_ref[0:19] == '/descubra/noticias/' or post_ref[0:6] == '/viaje':
            post_ref = 'https://www.carris.pt' + post_ref
        post_title = post.find('div', class_='subtitle left').text.strip()        
        if post_ref not in db.keys():
            print(f'{post_title}\n{post_ref}')
            print()
            additional_news += [[post_title, post_ref, 'CARRIS', 'https://i.ibb.co/hB0npQ1/carris.png', 943596807739551844]]
    if additional_news != []:
        for news in additional_news:
            db[news[1]] = ''
    print('find_c_news() ✅')
    return additional_news
  except Exception as error:
    global error_list
    if ['find_c_news() ❌', error] not in error_list:
        error_list = error_list + [['find_c_news() ❌', error]]
    print('find_c_news() ❌')
    return []


def find_ml_news_1():
  try:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    html_text = requests.get('https://www.metrolisboa.pt/informar-3/noticias/', headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('h2', class_='entry-title')
    additional_news = []
    for post in posts:
        post_title = post.a.text.strip()
        post_ref = post.a['href']
        if post_ref not in db.keys():
            print(f'{post_title}\n{post_ref}')
            print()
            additional_news += [[post_title, post_ref, 'Metropolitano de Lisboa', 'https://i.ibb.co/bQctjmf/metro.png', 943596738135097344]]
    if additional_news != []:
        for news in additional_news:
            db[news[1]] = ''
    print('find_ml_news_1() ✅')
    return additional_news
  except Exception as error:
    global error_list
    if ['find_ml_news_1() ❌', error] not in error_list:
        error_list = error_list + [['find_ml_news_1() ❌', error]]
    print('find_ml_news_1() ❌')
    return []


def find_ml_news_2():
  try:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    html_text = requests.get('https://www.metrolisboa.pt/institucional/comunicar/comunicados/', headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('h2', class_='entry-title')
    additional_news = []
    for post in posts:
        post_title = post.a.text.strip()
        post_ref = post.a['href']
        if post_ref not in db.keys():
            print(f'{post_title}\n{post_ref}')
            print()
            additional_news += [[post_title, post_ref, 'Metropolitano de Lisboa', 'https://i.ibb.co/bQctjmf/metro.png', 943596738135097344]]
    if additional_news != []:
        for news in additional_news:
            db[news[1]] = ''
    print('find_ml_news_2() ✅')
    return additional_news
  except Exception as error:
    global error_list
    if ['find_ml_news_2() ❌', error] not in error_list:
        error_list = error_list + [['find_ml_news_2() ❌', error]]
    print('find_ml_news_2() ❌')
    return []


def find_uniarea_news():
  try:
    html_text = requests.get('https://uniarea.com/category/noticias/').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('h2', class_='title cb-post-title')
    additional_news = []
    for post in posts:
        post_title = post.a.text.strip()
        post_ref = post.a['href']
        if post_ref not in db.keys():
            print(f'{post_title}\n{post_ref}')
            print()
            additional_news += [[post_title, post_ref, 'Uniarea', 'https://i.ibb.co/KVtT4Fs/uniarea.png', 943596874965872670]]
    if additional_news != []:
        for news in additional_news:
            db[news[1]] = ''
    print('find_uniarea_news() ✅')
    return additional_news
  except Exception as error:
    global error_list
    if ['find_uniarea_news() ❌', error] not in error_list:
        error_list = error_list + [['find_uniarea_news() ❌', error]]
    print('find_uniarea_news() ❌')
    return []


def find_tst_news():
  try:
    html_text = requests.get('https://www.tsuldotejo.pt/index.php?page=noticias').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('h2')
    additional_news = []
    for post in posts:
        post_title = post.a.text.strip()
        post_ref = 'https://www.tsuldotejo.pt/' + post.a['href']
        if post_ref not in db.keys():
            print(f'{post_title}\n{post_ref}')
            print()
            additional_news += [[post_title, post_ref, 'TST', 'https://i.ibb.co/K0X2JTk/tst.png', 943596845878345788]]
    if additional_news != []:
        for news in additional_news:
            db[news[1]] = ''
    print('find_tst_news() ✅')
    return additional_news
  except Exception as error:
    global error_list
    if ['find_tst_news() ❌', error] not in error_list:
        error_list = error_list + [['find_tst_news() ❌', error]]
    print('find_tst_news() ❌')
    return []


def find_fertagus_news():
  try:
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.fertagus.pt/Fertagus-pt/Viajar/Comunicados-e-Campanhas')
    additional_news = []
    sleep(5)
    for n in range(2, 6):
        try:
            post = driver.find_element(By.XPATH, f'//*[@id="divPages"]/div[{n}]/div[2]/div[2]/div/h2/strong/span')
            post_title = post.get_attribute("innerText")
            post_img = driver.find_element(By.XPATH, f'//*[@id="divPages"]/div[{n}]/div[2]/div[2]/a')
            post_ref = post_img.get_attribute("href")
            if post_ref not in db.keys():
                print(f'{post_title}\n{post_ref}')
                print()
                additional_news += [[post_title, post_ref, 'Fertagus', 'https://i.ibb.co/3SNHFCk/fertagus.png', 943596830036467742]]
        except:
            pass
    driver.quit()
    if additional_news != []:
        for news in additional_news:
            db[news[1]] = ''
    print('find_fertagus_news() ✅')
    return additional_news
  except Exception as error:
    global error_list
    if ['find_fertagus_news() ❌', error] not in error_list:
        error_list = error_list + [['find_fertagus_news() ❌', error]]
    print('find_fertagus_news() ❌')
    return []


def error_test():
  try:
    html_text = requests.get('https://www.fewfefowpjefifmklewmfkwemfweiofmewiçojwifwiefpio.com/').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('h2')
    additional_news = []
    for post in posts:
        post_title = post.a.text.strip()
        post_ref = 'https://www.tsuldotejo.pt/' + post.a['href']
        if post_ref not in db.keys():
            print(f'{post_title}\n{post_ref}')
            print()
            additional_news += [[post_title, post_ref, 'Transportes Sul do Tejo', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNaXVTLTNR8R-wjKCMisxvm0uX5lGtqVXLg2k66z36igXHMH4lMMksXzwIeAdxij2zeaY&usqp=CAU']]
    if additional_news != []:
        for news in additional_news:
            db[news[1]] = ''
    print('error_test() ✅')
    return additional_news
  except Exception as error:
    global error_list
    if ['error_test() ❌', error] not in error_list:
        error_list = error_list + [['error_test() ❌', error]]
    print('error_test() ❌')
    return []


def find_errors():
    global error_list
    return error_list


def reset_error_list():
    global error_list
    error_list = []


def find_all_news():
    return find_ml_news_1() + find_ml_news_2() + find_rl_news() + find_c_news() + find_uniarea_news() + find_tst_news() + find_fertagus_news() + find_website_news()
