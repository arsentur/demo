DBfile = 'text'

def open_file():
    with open(DBfile) as data:
        return data.read()

def write_file(value):
    with open(DBfile, 'a') as data:
        data.write(value + '\n')


if __name__ == '__main__':
    write_file('hello')
    print(open_file())