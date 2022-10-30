word_without_vowels = ""
user_word = input("Please enter the word: ")
user_word = user_word.upper()

# Prompt the user to enter a word
# and assign it to the user_word variable.
for x in user_word:
    if x not in ('A', 'E', 'I', 'O', 'U'):
        word_without_vowels += x
print(word_without_vowels)


# Print the word assigned to word_without_vowels.
