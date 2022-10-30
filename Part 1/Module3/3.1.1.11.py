income = float(input("Enter the annual income: "))

#
# Write your code here.
#
limit = 85_528
if income <= limit:
    tax = income * 0.18 - 556.02
else:
    tax = 14_839.02 + (income - limit) * 0.32

if tax <= 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
