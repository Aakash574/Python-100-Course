from audioop import avg


student_heights = [180, 124, 165, 173, 189, 169, 146]
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

for i in student_heights:
    totalHeight = sum(student_heights)
avg = totalHeight / (len(student_heights))
print(round(avg))
