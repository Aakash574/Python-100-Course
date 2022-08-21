# 🚨 Don't change the code below 👇
from pdb import post_mortem
from tkinter import HORIZONTAL, VERTICAL
from turtle import pos


row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
position = position
treasreHide = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
# if treasreHide[0][0] == position:
#     map[0][0] = "x"
# print(map)
hori = int(position[0])
ver = int(position[1])
# print(map[ver])

map[hori-1][ver-1] = "x"

# for i in range(len(map)):
#     for j in range(len(map)):
#         if treasreHide[i][j] == position:
#             map[i][j] = "x"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
