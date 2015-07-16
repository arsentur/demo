# coding: utf8

'''
1) важно делать проверку на существование папки
2) указывать полный путь не часто приходится, поэтому лучше получить текущую
папку
3) понятно как сделал, сейчас покажу как лучше сделать
'''

import csv
import os
from zipfile import *

PATH_TO_RATES = 'D:\Downloads\historical_exchange_rates.zip'
PATH_ZIP = os.getcwd() + '\extracted'


def decompression(whence):
    ZipFile(whence).extractall(PATH_ZIP)


def read_csv(file):
    with open(file) as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row['date;course'].split(';') for row in reader]

    return data


def operation(data):
    curse, all_base = [], []

    # exit(data[0])

    for elem in data:
        for k in elem[1::2]:
            curse.append(float(k))

        for n in elem:
            all_base.append(n)

    max_ = str(max(curse))
    min_ = str(min(curse))  # названия плохие

    for names in os.listdir(PATH_ZIP):
        print('В валюте: {}'.format(names[:-4]).upper())

        print('Самый высокий показатель:', all_base[all_base.index(max_)],
              'Был зафиксирован:', all_base[all_base.index(max_)-1])

        print('Самый низкий показатель:', all_base[all_base.index(min_)],
              'Был зафиксирован:', all_base[all_base.index(min_)-1])

        print()

if __name__ == '__main__':
    if not os.path.exists(PATH_ZIP):
        exit('Папка "{}" не существует.'.format(PATH_ZIP))

    decompression(PATH_TO_RATES)

    for file_name in os.listdir(PATH_ZIP):
        path = PATH_ZIP + '\\' + file_name

        operation(read_csv(path))
