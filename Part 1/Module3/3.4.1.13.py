list = []
list.append('John Lennon')
list.append('Paul McCartney')
list.append('George Harrison')

list2 = ['Stu Sutcliffe', 'Pete Best']
for i in list2:
    list.append(i)

del list[list.index('Stu Sutcliffe')]
list.insert(0, 'Ringo Starr')
print(list)
