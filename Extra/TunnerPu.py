# Left Angle Triangle
print("Left Angle Triangle")

for i in range(6):
    print(" *"*i)

# Right Angle Triangle
print("Right Angle Triangle")
j = 6
for i in range(6):
    j -= 1
    print("  "*j+" *"*i)

# Upside Down Right Angle Triangle
print("Upside Down Right Angle Triangle\n")
j = 6
for i in range(6):
    j -= 1
    print("  "*i+" *"*j)

# Upside Down Left Angle Triangle
print("Upside Down Left Angle Triangle\n")
j = 6
for i in range(6):
    j -= 1
    print(" *"*j)

# Triangle Pattern
print("Triangle Pattern")
j = 6
for i in range(6):
    j -= 1
    print(f" "*j+" *"*i)

# Numbering Programs
num = 1
for i in range(5):
    for j in range(i+1):
        print(num, end=" ")
        num += 1
    print("")

# Alphabat pattern Program
num = 65
for i in range(5):
    for j in range(i+1):
        ch = chr(num)
        print(ch, end=" ")
        num += 1
    print("\r")
