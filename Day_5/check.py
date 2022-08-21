from cgitb import strong
import random
from turtle import st
l = int(input())
n = int(input())
m = int(input())
o = int(input())
strongPassword = []
alphabates = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()-"
for i in range(n):
    ab = random.randrange(0, 25)
    strongPassword.append(alphabates[ab])
for i in range(m):
    ab = random.randrange(26, 51)
    strongPassword.append(alphabates[ab])
    # print(alphabates[ab], end="")
for i in range(o):
    sy = random.randint(0, 11)
    strongPassword.append(symbols[sy])
    # print(symbols[sy], end="")
print(strongPassword)
for i in range(l):
    passWord = random.random(0, l)

for i in strongPassword:
    print(passWord)
