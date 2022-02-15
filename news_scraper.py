import requests
from bs4 import BeautifulSoup
from replit import db


error_list = []


def write_all_rl_news():
    html_text = requests.get('https://www.rodoviariadelisboa.pt/comunicados').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('a', class_='titulo')
    for post in posts:
        post_ref = 'https://www.rodoviariadelisboa.pt/' + post['href']
        db[post_ref] = ''
    print('write_all_rl_news() ✅')


def find_rl_news():
  try:
    html_text = requests.get('https://www.rodoviariadelisboa.pt/comunicados').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('a', class_='titulo')
    additional_news = []
    for post in posts:
        post_title = post.text.strip().replace('Ã§', 'ç').replace('Ã£', 'ã').replace('Ã¡', 'á').replace('Ãµ', 'õ').replace('Ã¢', 'â')
        post_ref = 'https://www.rodoviariadelisboa.pt/' + post['href']
        if post_ref not in db.keys():
            print(f'{post_title}\n{post_ref}')
            print()
            additional_news += [[post_title, post_ref, 'Rodoviária de Lisboa', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTahAXa13o9NTAFvDIQCHBi7IxO3Z6f09_35LU85S7BmWYSkSn2bZnhnX-1f-LRv-4I-rs&usqp=CAU']]
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


def write_all_c_news():
    html_text = requests.get('https://www.carris.pt/descubra/noticias/informacoes-de-servico/').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('div', class_='container widget')
    for post in posts:
        post_ref = post.find('div', class_='col-12 col-md-6 image-block order-md-1').a['href']
        if post_ref[0:19] == '/descubra/noticias/' or post_ref[0:6] == '/viaje':
            post_ref = 'https://www.carris.pt' + post_ref
        db[post_ref] = ''
    print('write_all_c_news() ✅')


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
            additional_news += [[post_title, post_ref, 'CARRIS', 'https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/46/6b/62/466b621e-74bf-3d1a-0d83-a006dd8d8010/AppIcons-1x_U007emarketing-0-4-0-0-85-220.png/230x0w.webp']]
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


def write_all_ml_news_1():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    html_text = requests.get('https://www.metrolisboa.pt/informar-3/noticias/', headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('h2', class_='entry-title')
    for post in posts:
        post_ref = post.a['href']
        db[post_ref] = ''
    print('write_all_ml_news_1() ✅')


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
            additional_news += [[post_title, post_ref, 'Metropolitano de Lisboa', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Lisbon_Metro_logo.png/1200px-Lisbon_Metro_logo.png']]
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


def write_all_ml_news_2():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    html_text = requests.get('https://www.metrolisboa.pt/institucional/comunicar/comunicados/', headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('h2', class_='entry-title')
    for post in posts:
        post_ref = post.a['href']
        db[post_ref] = ''
    print('write_all_ml_news_2() ✅')


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
            additional_news += [[post_title, post_ref, 'Metropolitano de Lisboa', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Lisbon_Metro_logo.png/1200px-Lisbon_Metro_logo.png']]
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


def write_all_uniarea_news():
    html_text = requests.get('https://uniarea.com/category/noticias/').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('h2', class_='title cb-post-title')
    for post in posts:
        post_ref = post.a['href']
        db[post_ref] = ''
    print('write_all_rl_news() ✅')


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
            additional_news += [[post_title, post_ref, 'Uniarea', 'https://uniarea.com/wp-content/uploads/2014/06/logouniareafacebook4.png']]
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


def write_all_tst_news():
    html_text = requests.get('https://www.tsuldotejo.pt/index.php?page=noticias').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('h2')
    for post in posts:
        post_ref = 'https://www.tsuldotejo.pt/' + post.a['href']
        db[post_ref] = ''
    print('write_all_tst_news() ✅')


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
            additional_news += [[post_title, post_ref, 'Transportes Sul do Tejo', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNaXVTLTNR8R-wjKCMisxvm0uX5lGtqVXLg2k66z36igXHMH4lMMksXzwIeAdxij2zeaY&usqp=CAU']]
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


def write_all_news():
    write_all_ml_news_1()
    write_all_ml_news_2()
    write_all_rl_news()
    write_all_c_news()
    write_all_uniarea_news()


def find_errors():
    global error_list
    return error_list


def reset_error_list():
    global error_list
    error_list = []


def find_all_news():
    return find_ml_news_1() + find_ml_news_2() + find_rl_news() + find_c_news() + find_uniarea_news() + find_tst_news()