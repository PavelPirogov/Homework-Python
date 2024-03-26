"""Написать программу, которая скачивает изображения с заданных URL-адресов
и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
файле, название которого соответствует названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске:
image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный
подходы.
— Программа должна иметь возможность задавать список URL-адресов через
аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого
изображения и общем времени выполнения программы."""
import argparse
import asyncio
import os
import threading
import time
from multiprocessing import Process

import aiohttp
import requests

PATH = 'images'
images = []

with open('images.txt', 'r', encoding='utf-8') as img_file:
    for image in img_file.readlines():
        images.append(image.strip())


def download_image(url, dir_path=PATH):
    start_time = time.time()
    response = requests.get(url)
    filename = url.split('/')[-1]
    with open(os.path.join(dir_path, filename), 'wb') as file:
        for data in response.iter_content(1024):
            file.write(data)
    print(f'Загрузка {filename} заняла {time.time()- start_time:.2f} cекунд')


def thread_downloading(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_image, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(f'Итого: {time.time()- start_time:.2f} cекунд')


def multiprocess_download(urls):
    processes = []
    start_time = time.time()
    for url in urls:
        process = Process(target=download_image, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    print(f'Итого: {time.time()- start_time:.2f} cекунд')


async def download_image_async(url, dir_path=PATH):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            filename = url.split('/')[-1]
            with open(os.path.join(dir_path, filename), 'wb') as file:
                file.write(data)
    print(f'Загрузка {filename} заняла {time.time()- start_time:.2f} cекунд')


async def async_download(urls):
    tasks = []
    start_time = time.time()
    for url in urls:
        task = asyncio.create_task(download_image_async(url))
        tasks.append(task)
        await asyncio.gather(*tasks)
    print(f'Итого: {time.time()- start_time:.2f} cекунд')


def parse():
    parser = argparse.ArgumentParser(
        description='Парсер изображений по URL-адресам')
    parser.add_argument('-u', '--urls', default=images,
                        nargs='+', type=str, help='Список URL-адресов')
    return parser.parse_args()


if __name__ == '__main__':
    urls = parse().urls
    if not os.path.exists(PATH):
        os.mkdir(PATH)
    print(f'Загрузка {len(urls)} изображений через потоки: ')
    thread_downloading(urls)
    print()
    print(f'Загрузка {len(urls)} изображений через процессы: ')
    multiprocess_download(urls)
    print()
    print(f'Загрузка {len(urls)} изображений асинхронно: ')
    asyncio.run(async_download(urls))
