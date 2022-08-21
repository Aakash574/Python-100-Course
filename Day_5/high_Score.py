# from tkinter.tix import MAX


from xml.dom.minidom import Element


ss = [78, 65, 89, 86, 55, 100, 91, 64, 89]

# Sorting the list of score and return last Element in the list
# In this case the last element is high Score
# Code -
# Sorted_Student_Score = sorted(student_scores)
# print(Sorted_Student_Score[-1])
ms = 0

for i in range(len(ss)):
    if ms < ss[i]:
        ms = ss[i]
print(ms)
