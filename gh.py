# coding: utf8

"""
Задача:

Разделить строку (2) через запятую, убрать числа, пробелы (пустые элементы имеется), и слова с заглавной буквы.
Потом снова привести в строку разделенную запятой.

Ошибки:

1) перебирать посимвольно - неправильно изначально. все предложения разделены запятой, по не и нужно делить

Разбор задачи:

1. Разбиваем имеющиюся строку через запятую
2. Напишем функцию, которая будет убирать числа в каждом элементе
3. Очищаем каждый элемент от пробелов слева и справа - метод .strip()
4. Удаляем (пропускаем) пустые элементы
5. Пропускаем элементы с заглавной буквы
6. Снова разделяем запятой

"""

import string


my_string = 'Мама, папа, деда, , баба, 144 лет, Огород, не хочу, а нужно.'
uppers = string.ascii_uppercase + 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def is_upper(value):
    for char in value:
        if char in uppers:
            return True

    return False


def remove_digits(item):
    for digit in string.digits:
        item = item.replace(digit, '')

    return item


def change_str(value):
    final = []

    for item in value.split(','):
        item = remove_digits(item).strip()
        if len(item) and not is_upper(item): # наверно только англ пропускает
            final.append(item)

    return ', '.join(final)


print(change_str(my_string))
