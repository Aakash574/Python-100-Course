import random
from secrets import choice

lst = ["Aakash", "Manish", "Sumit", "Ganesh"]
choice = random.randint(0, 3)
print(f"{lst[choice]} is going to pay todays Bill")
