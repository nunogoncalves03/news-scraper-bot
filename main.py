import os
import wget


try:
    os.remove('news_scraper.py')
    news_scraper_file = wget.download('https://raw.githubusercontent.com/nunogoncalves03/news-scraper-bot/main/news_scraper.py')
    os.remove('discord_bot.py')
    discord_bot_file = wget.download('https://raw.githubusercontent.com/nunogoncalves03/news-scraper-bot/main/discord_bot.py')
except:
    print('news_scraper.py ❌\ndiscord_bot.py ❌')

os.system('python redirect_to_main.py')
