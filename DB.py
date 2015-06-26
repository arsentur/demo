DBfile = 'text'

def open_file():
    with open(DBfile) as data:
        return data.read().splitlines()

def write_file(value):
    with open(DBfile, 'a') as data:
        data.write(value + '\n')

def remove_element(n):
    DB = open_file()
    del DB[n]
    with open(DBfile, 'w') as data:
        for n, iter in enumerate(DB):
            data.write(iter + '\n')

def edit(new_val,n):
    DB = open_file()
    DB.insert(n,new_val)
    with open(DBfile, 'w') as data:
        for n, iter in enumerate(DB):
            data.write(iter + '\n')




if __name__ == '__main__':
    # write_file('hello')
    print(open_file())