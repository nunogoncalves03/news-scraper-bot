import os
import wget


try:
    os.remove('news_scraper.py')
    news_scraper_file = wget.download('https://raw.githubusercontent.com/nunogoncalves03/news-scraper-bot/main/news_scraper.py')
    print(f'\n{news_scraper_file} ✅')
    os.remove('discord_bot.py')
    discord_bot_file = wget.download('https://raw.githubusercontent.com/nunogoncalves03/news-scraper-bot/main/discord_bot.py')
    print(f'\n{discord_bot_file} ✅')
except:
    print('news_scraper.py/discord_bot.py ❌')

