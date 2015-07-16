# coding: utf8

data = [elem for elem in range(0, 1000, 50)]
result = [data[n] * data[n-1] for n in range(2, len(data))]


def save_db():
    with open('result.txt', 'w') as file:
            file.writelines([str(el) + '\n' for el in result])

print(result)
print(data)
save_db()
