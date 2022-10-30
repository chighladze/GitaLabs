blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#
i = 1
count = 0
while 1:
    blocks = blocks - i
    i += 1
    if blocks == 0:
        count += 1
        break
    if blocks < 0:
        break
    count += 1

height = count

print("The height of the pyramid:", height)
