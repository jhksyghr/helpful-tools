from jhk_imports import *

ind = 'ind_rename.txt'


def code():
    fo = open(ind_self, 'w')
    files = my_list_all_txt_files(folder, [], [ind, '.py'], [])
    i = 0
    for fi, file in enumerate(files):
        print('\r' + str(fi) + ' % ' + str(files.__len__()), end='')
        fo.writelines(file + '\n')
        os.rename(file, file[:1 + file.find(my_get_level_dir(file, 1))] + '%04d' % i + '.bin')
        i = i + 1
    fo.close()


def decode():
    fo = open(ind_self, 'r+')
    files = my_list_all_txt_files(folder, ['.bin'], [])
    for fi, file in enumerate(files):
        x = fo.readline(300)
        if x == '':
            break
        os.rename(file, x[:-1])
        print('\r' + str(fi) + ' % ' + str(files.__len__()), end='')
    fo.close()
    os.remove(ind_self)


if __name__ == '__main__':
    folder = r'D:\test_py_folder\190918'
    fs = my_list_all_txt_files(folder, ['.txt'], [], [])
    ind_self = os.path.join(folder, ind)

    if ind_self in fs:
        decode()
    else:
        code()
