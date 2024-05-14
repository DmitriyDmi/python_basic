"""
2. Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.
"""


import os
import pandas as pd
import pickle
from os.path import getsize, join

directory = 'C:\\Users\\р\\python_lessons\\7'


dir_sizes = {'object': [], 'path': [], 'type': [], 'size': []}


def dir_skan(directory = '.'):
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            dir_sizes['object'].append(file)
            dir_sizes['path'].append(root)
            dir_sizes['type'].append('file')
            dir_sizes['size'].append(getsize(join(root, file)))
        size = sum(getsize(join(root, f)) for f in files)
        size += sum(dir_sizes['size'][dir_sizes['object'].index(join(root, d))] for d in dirs)

        dir_sizes['object'].append(root)
        dir_sizes['path'].append(root.rsplit(sep='\\', maxsplit=0)[0])
        dir_sizes['type'].append('dir')
        dir_sizes['size'].append(size)
    df = pd.DataFrame(dir_sizes)
    df.to_csv('csv_dir_size.csv', index=False)
    df.to_json('json_dir_size.json', orient='records')
    with open('picklie_dir_size.pkl', 'wb') as f:
        pickle.dump(dir_sizes, f)


if __name__ == '__main__':
    dir_skan(directory)