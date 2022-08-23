l = [3, 4, 5, 1.3, 'zebra', 'goat',
     'ant', 'elephant', 'buffalo', -67, 78]
temp = []
for i in range(len(l)):
    if type(l[i]) != str:
        if l[i] <= 0 or l[i] >= 0:
            temp.append(l[i])
print(temp)
