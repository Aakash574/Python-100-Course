import string
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

true = name1.count("t") + name2.count("t") + name1.count("u") + name2.count("u") + \
    name1.count("r") + name2.count("r") + name1.count("e") + name2.count("e")

Love = name1.count("l") + name2.count("l") + name1.count("v") + name2.count("v") + \
    name1.count("e") + name2.count("e")+name1.count("o") + name2.count("o")

totalScore = int(f"{true}{Love}")
if totalScore < 10 or totalScore > 90:
    print(f"Your Score is {totalScore}, You live together forever")
elif totalScore > 40 and totalScore < 50:
    print(f"Your Score is {totalScore}, You always together")
else:
    print(f"Your Score is {totalScore}")
