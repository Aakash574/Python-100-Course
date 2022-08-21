from cgitb import strong
import random
from symtable import Symbol


def passwordGenrator():
    print("Welcome to the pypassword Generator!")
    strongPassword = 0
    passwordLen = int(
        input("How many letters would you like to your password?\n"))
    symbol = int(input("How many symbols would you like?\n"))
    numbers = int(input("How many numbers would you like?\n"))
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

    print(f"{strongPassword}")
