import requests as req
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
import os
import csv
import time


def bootstrap_parser():
    if not os.path.exists('news.csv'):
        with open('news.csv', 'w') as f:
            csv_header = ['Time', 'Title', 'Text', 'Url']
            writer = csv.writer(f)
            writer.writerow(csv_header)
    else:
        with open('news.csv', encoding='utf-8') as news:
            news = {row[3] for row in news}
    
    session = req.Session()
    session.headers.update({'user-agent': UserAgent().random,})

    try:
        cooldown = int(input("Введите время в секундах для проверки новостей: "))
        if cooldown <= 0:
            raise ValueError("Задержка должна быть больше 0.")
    except ValueError as e:
        cooldown = 300
        print(f"{e}")
        print("Установлено значение по умолчанию: 300 секунд.")
    
    return session, news, cooldown
        

def get_news(session, past_news: set) -> set:
    
    source_url = 'https://www.benzinga.com'
    market_url = source_url + '/markets'
    
    try:
        response = session.get(market_url, timeout=10)
        response.raise_for_status()
    except req.RequestException as e:
        print(f"Ошибка: {e}")
        return set()

    html = BS(response.text, 'html.parser')
    news = html.select('.flex.flex-col.justify-between.w-full .text-\\[inherit\\]')
    res = {
        "time": [],
        "titles": [],
        "text": [],
        "urls": [],
    }
    
    for new in news:
        href = new.get('href')
        if not href:
            continue

        title_tag = new.select_one('.inline')
        if not title_tag:
            continue

        title = title_tag.get_text(strip=True)
        url = source_url + href

        if url in past_news:
            continue

        res['titles'].append(title)
        res['urls'].append(url)

    if res['urls'] == []:
        return set()

    for url in res['urls']:
        try:
            resp = session.get(url, timeout=10)
            resp.raise_for_status()
        except req.RequestException as e:
            print(f"Ошибка: {e}")
            continue
        
        html_txt = BS(resp.text, 'html.parser')
        sentences = html_txt.select('.block.core-block')
        text = [sentence.text for sentence in sentences[:-3]]
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        
        res['text'].append(' '.join(text))
        res['time'].append(current_time)

        time.sleep(1)

    with open('news.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)

        ready_news = list(zip(*res.values()))
        writer.writerows(ready_news)

    return set(res['urls'])


session, news, cooldown = bootstrap_parser()

while True:
    news |= get_news(session, news)
    print(news)
    time.sleep(cooldown)