def is_anagram(a, b):
    if sorted(a.lower()) == sorted(b.lower()):
        return 'Anagrams'
    else:
        return 'Not anagrams'


print(is_anagram('Listen', 'Silent'))
print(is_anagram('modern', 'norman'))
