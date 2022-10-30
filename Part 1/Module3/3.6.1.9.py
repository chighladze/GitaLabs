my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)
    else:
        continue

""" most better"""
# new_list = list(set(my_list)) <<<<<<<<<<<<<<<<<<<<<<

print("The list with unique elements only:")
print(new_list)
