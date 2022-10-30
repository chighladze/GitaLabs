def mysplit(strng):
    lst = []
    str = ""
    for i in strng:
        if i != " ":
            str += i
        else:
            lst.append(str)
            str = ""
    return lst


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
