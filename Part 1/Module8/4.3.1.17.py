from os import strerror


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self, message)


class FileEmpty(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self, message)


input = ''
dct = {}
fullname = ''
file_name = "notebook.txt"

try:
    src = open(file_name, "rt")
    input = src.readlines()
    src.close()
    if len(input) == 0:
        raise FileEmpty("The is empty")
    for x in range(len(input)):
        tem = input[x].split()
        if len(tem) != 3:
            raise BadLine("BadLine: " + str(x + 1))
        fullname = tem[0] + ' ' + tem[1]
        if fullname not in dct:
            dct[fullname] = float(tem[2])
        else:
            dct[fullname] += float(tem[2])
except FileEmpty as fe:
    print(fe)
except BadLine as bl:
    print(bl)
except IOError as e:
    print("Cannot open file: ", strerror(e.errno))


for x in sorted(dct.keys()):
    print(x, dct[x])
