import os

ind = 'ind.txt'


def code():
    files = os.listdir()
    if os.path.exists(ind):
        os.remove(ind)
    f = open(ind, 'w')
    i = 0
    for file in files:
        if file.find('.txt') != -1:
            continue
        if file.find('.py') != -1:
            continue
        print(file)
        f.writelines(file + '\n')
        os.rename(file, str(i) + '.bin')
        i = i + 1
    f.close()


def decode():
    f = open(ind, 'r+')
    i = 0
    while 1:
        x = f.readline(100)
        if x == '':
            break
        os.rename(str(i) + '.bin', x[:-1])
        i = i + 1
        print(x)


if __name__ == '__main__':
    # code()
    decode()