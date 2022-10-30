import os


def find_dir(path, dir):
    cd = os.listdir(path)
    lst = []
    if dir in cd:
        lst.append(f'{path}/{dir}')
    for i in cd:
        new_path = f'{path}/{i}'
        if i != dir:
            find_dir(new_path, dir)
    if len(lst) > 0:
        print(lst[0])


path = 'tree'
dir = 'python'

find_dir(path, dir)
