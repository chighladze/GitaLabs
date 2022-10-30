def read_int(prompt, min, max):
    lst = list(range(min, max))
    if prompt in lst:
        return 'The number is permitted range'
    else:
        return 'Error: (min..max)'


while 1:
    prompt = input('enter a number: ')
    min  = input('enter a min number: ')
    max = input('enter a max number: ')

    try:
        prompt = int(prompt)
        min = int(min)
        max = int(max)
        if type(prompt) == int and type(min) == int and type(max) == int:
            print(read_int(prompt, min, max))
    except:
        print('Error, wrong input')


