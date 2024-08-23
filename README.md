---
# AnimeGO-parser

Этот проект предназначен для парсинга аниме с сайта AnimeGO. Он автоматически собирает данные о новых аниме, включая названия, жанры, описания и ссылки, и сохраняет их в формате JSON и CSV. Проект включает в себя скрипт на Python, который выполняет следующие задачи:

1. **Скачивание данных с сайта AnimeGO.**
2. **Извлечение информации о каждом аниме.**
3. **Сохранение данных в два формата: JSON и CSV.**
4. **Обновление файлов с данными по мере сбора новых страниц.**

## Как использовать

### 1. Установка зависимостей

Прежде чем начать, вам нужно установить необходимые зависимости. Убедитесь, что у вас установлен Python версии 3.x. Для установки зависимостей выполните следующую команду:

```bash
pip install -r requirements.txt
```

**Примечание:** Файл `requirements.txt` должен содержать список всех необходимых библиотек, таких как `requests`, `beautifulsoup4`. Если файл `requirements.txt` отсутствует, создайте его и добавьте в него следующие строки:

```plaintext
requests
beautifulsoup4
```

### 2. Настройка

Перед запуском скрипта убедитесь, что у вас есть доступ к папке для сохранения файлов. Скрипт будет сохранять данные в файлы `anime.json` и `anime.csv`, которые будут находиться в папке `anime-data`. Если эта папка не существует, она будет создана автоматически.

### 3. Запуск скрипта

Для парсинга данных и их сохранения выполните следующую команду:

```bash
python parser.py
```
Для Linux:

```bash
python3 parser.py
```

**Примечание:** Убедитесь, что вы находитесь в корневой директории проекта, где находится файл `parser.py`.

### 4. Форматы файлов

- **`anime.json`**: Файл в формате JSON, содержащий список объектов, каждый из которых представляет одно аниме. Каждый объект включает:
  - `"Anime"`: Название аниме.
  - `"Genres"`: Список жанров аниме.
  - `"Description"`: Описание аниме.
  - `"URL"`: Ссылка на страницу аниме на сайте AnimeGO.

- **`anime.csv`**: Файл в формате CSV, содержащий данные о каждом аниме. Структура файла включает следующие столбцы:
  - `ID`: Уникальный идентификатор аниме.
  - `Title`: Название аниме.
  - `Genres`: Список жанров, разделенных запятыми.
  - `Description`: Описание аниме.
  - `URL`: Ссылка на страницу аниме.

### Пример запуска

Если у вас установлен Python и зависимости настроены, запустите скрипт, используя следующую команду:

```bash
python parser.py
```

### Обновление данных

Каждый раз, когда вы запускаете скрипт, он будет:
1. Проверять наличие новых страниц аниме.
2. Парсить данные с новых страниц.
3. Обновлять файлы `anime.json` и `anime.csv` с новыми данными.

### Лицензия

Этот проект лицензирован под MIT License. Подробности можно найти в файле `LICENSE` в корневой директории проекта.

### Контрибьюции

Если вы хотите внести изменения в проект, пожалуйста, создайте Pull Request с описанием ваших изменений. Я приветствую любой вклад в улучшение проекта!

---
