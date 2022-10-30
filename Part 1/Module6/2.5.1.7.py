def palindrome_or_not(txt: str):
    lst = []
    for i in txt:
        if i != ' ':
            lst.append(i.lower())
    if lst[::-1] == lst:
        return 'It\'s a palindrome'
    else:
        return 'It\'s not a palindrome'


print(palindrome_or_not('Ten animals I slam in a net'))
print(palindrome_or_not('Eleven animals I slam in a net'))
