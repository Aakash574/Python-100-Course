# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = extra_cheese.upper()
# print(f"{size} {add_pepperoni} {extra_cheese}")
totalBill = 0
if size == 'S':
    totalBill += 15
    if add_pepperoni == 'Y':
        totalBill += 2
elif size == 'M':
    totalBill += 20
    if add_pepperoni == 'Y':
        totalBill += 3
else:
    totalBill += 25
    if add_pepperoni == 'Y':
        totalBill += 3

if extra_cheese == 'Y':
    totalBill += 1

print(f"Your final bill is: ${totalBill}")
