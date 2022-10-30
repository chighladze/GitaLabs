user_word = input("please enter the word: ")
user_word = user_word.upper()

for x in user_word:
    if x not in ('A', 'E', 'I', 'O', 'U'):
        print(x)



