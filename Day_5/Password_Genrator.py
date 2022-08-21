from codecs import latin_1_decode
import random
from subprocess import NORMAL_PRIORITY_CLASS
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


passwordGenratad = []

for char in range(1, nr_letters+1):
    passwordGenratad.append(random.choice(letters))
for char in range(1, nr_symbols+1):
    passwordGenratad.append(random.choice(symbols))
for char in range(1, nr_numbers+1):
    passwordGenratad.append(random.choice(numbers))
# print(passwordGenratad)

random.shuffle(passwordGenratad)
password = ""
for char in passwordGenratad:
    password += char

print(password)
