import os
import platform
import shutil
import subprocess

import colorama
import requests
from bs4 import BeautifulSoup

# Функция создания папки, где будут храниться изображения постранично
def create_dir():
    os.mkdir(f'Pages')
    os.chdir('Pages')


# Функция открытия директории после успешного завершения работы кода
def open_dir(path: str):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


pages_count = input('How many pages do you want to parse: ')

print(f'{colorama.Fore.LIGHTYELLOW_EX}Wait few seconds...')

# После принятия значения количества необходимых страниц для парсинга, проверяем подходит ли нам это значение, если нет выводим исключение
try:

    # Создание папки
    # Если происходит исключение удаляем старую папку и создаем на ее месте другую
    try:
        create_dir()
    except FileExistsError:
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Pages')
        shutil.rmtree(path)
        create_dir()

    # Путь текущией директории
    path = os.getcwdb()

    for id_page in range(int(pages_count)):

        # Создаем папку для хранения данных
        os.mkdir(f'Page #{id_page + 1}')

        url = f'https://stopgame.ru/news/all/p{id_page + 1}'

        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'lxml')
        sequence_image_elements = soup.find_all('img', class_="image-16x9 p-0")

        for once_element in sequence_image_elements:

            # Узнаем alt-имя у фото
            alt_name = once_element.get('alt')
            alt_name = alt_name.replace(':', '')

            # Узнаем путь до фото
            src_link = once_element.get('src')

            # Сохраняем фото в папке
            with open(f'Page #{id_page + 1}/{alt_name}.jpg', 'wb') as handler:
                img_data = requests.get(src_link).content
                handler.write(img_data)

    # Информирование об успешном выполнении и открытие директории хранения данных
    print(f'{colorama.Fore.LIGHTGREEN_EX}✔ Complete')
    open_dir(path)


except* (TypeError, ValueError):
    print(f'Exception: Enter a numeric value, not another')