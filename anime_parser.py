from bs4 import BeautifulSoup
from random import uniform
import requests
import json
import csv
import os
import time

def fetch_page_data(page):
    url = f'https://animego.me/anime/{page}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:129.0) Gecko/20100101 Firefox/129.0",
        "Accept": "*/*"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text


def parse_anime_data(page_content):
    soup = BeautifulSoup(page_content, 'lxml')
    anime_blocks = soup.find_all('div', class_='ani-list__item')
    anime_data_list = []

    for anime in anime_blocks:
        title_div = anime.find('div', class_='ani-list__item-title')
        link_tag = title_div.find('a') if title_div else None
        if not link_tag:
            continue

        title = link_tag.text.strip()
        url = link_tag['href']

        desc_tag = anime.find('div', class_='ani-list__item-description')
        description = desc_tag.text.strip() if desc_tag else ''

        genres_container = anime.find('div', class_='ani-list__item-genres')
        genres = []
        if genres_container:
            for a in genres_container.find_all('a', class_='ani-list__item-genres__link'):
                if '/anime/genre/' in a.get('href', ''):
                    genres.append(a.text.strip())

        anime_data_list.append({
            "Title": title,
            "Genres": ', '.join(genres),
            "Description": description,
            "URL": url
        })

    return anime_data_list


def clear_files(json_filename, csv_filename):
    # Создаем директорию, если она не существует
    os.makedirs(os.path.dirname(json_filename), exist_ok=True)
    os.makedirs(os.path.dirname(csv_filename), exist_ok=True)

    # Очищаем JSON файл
    open(json_filename, 'w').close()

    # Очищаем CSV файл
    open(csv_filename, 'w').close()

def collect_all_anime_data(num_pages, json_filename, csv_filename):
    # Очищаем файлы перед началом сбора данных
    clear_files(json_filename, csv_filename)

    all_anime_data = []

    csv_file_exists = os.path.exists(csv_filename)
    for page in range(1, num_pages + 1):
        print(f"Fetching page {page}...")
        page_content = fetch_page_data(page)
        if page_content is None:
            print(f"Page {page} not found. Exiting.")
            break

        page_data = parse_anime_data(page_content)
        print(f"  Найдено тайтлов: {len(page_data)}")
        if not page_data:
            print("Пустая страница — похоже, конец каталога. Останавливаюсь.")
            break

        all_anime_data.extend(page_data)
        
        # Записываем обновленные данные в JSON файл
        with open(json_filename, 'w', encoding='utf-8') as file:
            json.dump(all_anime_data, file, indent=4, ensure_ascii=False)
        
        # Записываем данные в CSV файл постранично
        with open(csv_filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Записываем заголовки только если файл пуст
            if not csv_file_exists:
                writer.writerow(['#', 'Title', 'Genres', 'Description', 'URL'])
                csv_file_exists = True
            
            # Записываем данные текущей страницы
            start_index = len(all_anime_data) - len(page_data) + 1
            for i, anime in enumerate(page_data, start=start_index):
                writer.writerow([i, anime['Title'], anime['Genres'], anime['Description'], anime['URL']])
        
        time.sleep(uniform(0.3, 0.5))  # Задержка между запросами для предотвращения блокировки

# Запуск сбора данных
try:
    collect_all_anime_data(1000, "anime-data/anime.json", "anime-data/anime.csv")
except requests.exceptions.HTTPError:
    print(f"The end of the list reached")