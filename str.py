# coding: utf8
""" Почему ф-ция 1 не работает а вторая работает? Они отличаются только методом .format() """


def extract_from_tag(tag, line):
    opener = '< {} >'.format(tag)
    closer = '</ {} >'.format(tag)
    try:
        i = line.index(opener)
        start = i + len(opener)
        j = line.index(closer)
        return line[start:j]
    except ValueError:
        return None


def extract_from_tag_2(tag, line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    i = line.find(opener)
    if i != -1:
        start = i + len(opener)
        j = line.find(closer, start)
        if j != -1:
            return line[start:j]
    return None

print(extract_from_tag('red', 'what a <red> rose </red> this is'))


""" Метод str.partition() """

s = '/usr/local/bin/firefox'

i = s.rfind('/')
if i == -1:
    result = s, '', ''
else:
    result = s[:i], s[i], s[i + 1:]

result_1 = s.rpartition('/')
#print(result_1)

filename = 'photo.jpg'

if filename.lower().endswith(('.jpg', '.jpeg')):
    print('{} is a JPEG image'.format(filename))

table = ''.maketrans("\N{bengali digit zero}"
"\N{bengali digit one}\N{bengali digit two}"
"\N{bengali digit three}\N{bengali digit four}"
"\N{bengali digit five}\N{bengali digit six}"
"\N{bengali digit seven}\N{bengali digit eight}"
"\N{bengali digit nine}", "0123456789")

print("20749".translate(table))

print("\N{bengali digit two}3434\N{bengali digit four}"
"\N{bengali digit nine}".translate(table))