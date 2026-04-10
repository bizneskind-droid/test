import requests as req
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
import os
import time
import psycopg2
from psycopg2.extensions import connection
from psycopg2.extras import execute_values


def check_old_news(all_urls: list[str], DSN: str) -> set[str]:
    conn = psycopg2.connect(DSN)
    existing_urls = set()
    
    try:
        with conn, conn.cursor() as cur:
            cur.execute('''
                SELECT url FROM news
                WHERE url = ANY(%s)            
            ''', (all_urls,))
            
            existing_urls = {row[0] for row in cur.fetchall()}
        
    except psycopg2.Error as e:
        print(f"Database error: {e.pgcode} - {e.pgerror}")
    except Exception as e:
        print(f"Error: {type(e).__name__} - {e}")|
    finally:
        conn.close()
        
    return existing_urls
    
    
def create_db() -> str:
    DSN = "postgresql://test_user:123@localhost:5432/parser"
    conn = psycopg2.connect(DSN)
    
    try:
        with conn, conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS news (
                id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                time TIMESTAMP DEFAULT NOW(),
                title TEXT DEFAULT 'Nothing',
                text TEXT DEFAULT 'Nothing',
                url VARCHAR(300) UNIQUE
                );
        """)
        
    except psycopg2.Error as e:
        print(f"Database error: {e.pgcode} - {e.pgerror}")
    finally:
        conn.close()
        
    return DSN


def update_db(DSN: str, already_news: list) -> list[tuple[int, str]]:
    conn = psycopg2.connect(DSN)
    res = []
    
    try:
        with conn, conn.cursor() as cur:
            res = execute_values(
                cur, 
                '''
                INSERT INTO news (time, title, text, url)
                VALUES %s 
                ON CONFLICT (url) DO NOTHING
                RETURNING id, url;
                ''', already_news,
                fetch=True
                )           
        
    except psycopg2.Error as e:
        print(f"Database error: {e.pgcode} - {e.pgerror}")
    finally:
        conn.close()
        
    return res 
        
    
def bootstrap_parser():
    DSN = create_db()        
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
    
    return session, cooldown, DSN
        

def get_news(session: req.Session, DSN: str):
    
    source_url = 'https://www.benzinga.com'
    market_url = source_url + '/markets'
    
    try:
        response = session.get(market_url, timeout=10)
        response.raise_for_status()
    except req.RequestException as e:
        print(f"Ошибка: {e}")
        return 

    html = BS(response.text, 'html.parser')
    news = html.select('.flex.flex-col.justify-between.w-full .text-\\[inherit\\]')
    times = []
    texts = []
    temp_dict: dict[str, str] = {}
    all_urls = []
    res = []

    for new in news:
        href = new.get('href')
        if not href:
            continue

        title_tag = new.select_one('.inline')
        if not title_tag:
            continue

        title = title_tag.get_text(strip=True)
        url = source_url + href
        
        all_urls.append(url)
        temp_dict[url] = title
        
    existing_urls = check_old_news(all_urls, DSN)
    temp_dict = {
        url: title
        for url, title in temp_dict.items()
        if url not in existing_urls
    }

    if not temp_dict:
        return 

    for url, title in temp_dict.items():
        try:
            resp = session.get(url, timeout=10)
            resp.raise_for_status()
        except req.RequestException as e:
            print(f"Ошибка: {e}")
            continue
        
        html_txt = BS(resp.text, 'html.parser')
        sentences = html_txt.select('.block.core-block')
        text = [sentence.text for sentence in sentences[:-1]]
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        
        res.append((
        current_time,
        title,
        ' '.join(text),
        url
        ))

        time.sleep(1)


    return update_db(DSN, res)


if __name__ == "__main__":
    session, cooldown, DSN = bootstrap_parser()

    while True:
        try:
            latest_news = get_news(session, DSN)
            if latest_news:
                for news_id, url in latest_news:
                    print(f"Добавлена новость с id: {news_id}\nURL: {url}")
            else:
                print("Новостей нет.")
        except Exception as e:
            print(f"Критическая ошибка в главном цикле: {e}")
        
        time.sleep(cooldown)