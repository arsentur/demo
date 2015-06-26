DB_FILE = 'text'


def open_file():
    with open(DB_FILE) as data:
        return data.read().splitlines()


def write_file(value):
    with open(DB_FILE, 'a') as data:
        data.write(value + '\n')


def save_db(db):
    with open(DB_FILE, 'w') as data:
        for i in db:
            data.write(i + '\n')


def remove_element(n):
    db = open_file()
    del db[n]
    save_db(db)


def edit(new_val, n):
    db = open_file()
    db[n] = new_val
    save_db(db)


if __name__ == '__main__':
    print(open_file())