hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

hours = ((hour * 60 + mins + dura) // 60) % 24
minutes = ((hour * 60 + mins + dura) % 60) % 60

print(f'{hours}:{minutes}')
