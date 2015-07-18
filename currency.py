# coding: utf8

from zipfile import *
import csv
import os


for file in os.listdir('D:\PYTHON\Zipping'):
    pass

z = ZipFile('D:\Downloads\historical_exchange_rates.zip', 'r')
z.extractall()

curse = []
date = []

with open(file) as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row['date;course'].split(';') for row in reader]

for elem in data:
    for k in elem[1::2]:
        curse.append(float(k))
    for n in elem:
        date.append(n)

    max_ = max(curse)
    min_ = min(curse)

for file in os.listdir('D:\PYTHON\Zipping'):
    print('В валюте: {}'.format(file[:-4]).upper())
    print('Самый высокий показатель:', date[date.index(str(max_))],'Был зафиксирован:', date[date.index(str(max_))-1])
    print('Самый низкий показатель:', date[date.index(str(min_))],'Был зафиксирован:', date[date.index(str(min_))-1])
