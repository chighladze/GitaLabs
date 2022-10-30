secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")


while 1:
    user_num = int(input("Please enter your number: "))
    if secret_number == user_num:
        print("Well done, muggle! You are free now.")
    else:
        print("Ha ha! You're stuck in my loop!")


