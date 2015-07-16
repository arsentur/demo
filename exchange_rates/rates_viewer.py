# coding: utf8

'''
1) важно делать проверку на существование папки
2) указывать полный путь не часто приходится, поэтому лучше получить текущую
папку
3) понятно как сделал, сейчас покажу как лучше сделать
'''

import csv
import os
from statistics import median
from zipfile import ZipFile

PATH_TO_RATES = 'D:\Downloads\historical_exchange_rates.zip'
PATH_ZIP = os.getcwd() + '\extracted'


def decompression(whence):
    ZipFile(whence).extractall(PATH_ZIP)


def read_csv(file):
    with open(file) as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row['date;course'].split(';') for row in reader]

    return {el[0]: float(el[1]) for el in data}


def search_min_and_max_course(courses):
    sort_courses = sorted(courses.items(), key=lambda x: x[1])

    max_course = sort_courses[-1]
    min_course = sort_courses[0]

    return {'date': max_course[0], 'value': max_course[1]}, {'date': min_course[0], 'value': min_course[1]}


def show_information(course_name, course_data):
    median_course = median(course_data.values())
    max_course, min_course = search_min_and_max_course(course_data)

    print('В валюте: {}'.format(course_name))

    print('Самый высокий показатель:', max_course['value'],
          'Был зафиксирован:', max_course['date'])

    print('Самый низкий показатель:', min_course['value'],
          'Был зафиксирован:', min_course['date'])

    print('Медиана:', median_course)

    print()


if __name__ == '__main__':
    if not os.path.exists(PATH_ZIP):
        exit('Папка "{}" не существует.'.format(PATH_ZIP))

    decompression(PATH_TO_RATES)

    courses = {}
    for file_name in os.listdir(PATH_ZIP):
        course_name = file_name.replace('.csv', '').upper()
        courses[course_name] = read_csv(PATH_ZIP + '\\' + file_name)

    for course, data in courses.items():
        show_information(course, data)
