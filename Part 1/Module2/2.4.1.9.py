kilometers = 12.25
miles = 7.38
const = 1.61

miles_to_kilometers = miles * const
kilometers_to_miles = kilometers / const

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
