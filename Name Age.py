# coding=utf-8

FILE = 'test_data.txt'


def open_file():
    with open(FILE) as data:
        lines = data.read().splitlines()

    return lines


def file_conversion(value):
    final_list = []
    for elem in value:
        data = elem.split(';')
        for n in data:
            if '.' in n:
                try:
                    final_list.append(float(n))
                except ValueError:
                    pass
    print('Собственно сам список', final_list)
    print('Максимальный элемент списка: ', max(final_list))
    print('Минимальный элемент списка: ', min(final_list))
    print('Сумма списка: ', sum(final_list))


print(file_conversion(open_file()))
