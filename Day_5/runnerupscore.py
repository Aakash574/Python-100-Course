# # from operator import add


# # def addition(x):
# #     if x == 1:
# #         return 1
# #     else:
# #         return x * addition(x-1)


# # x = addition(5)
# # print(x)

# if __name__ == '__main__':
#     # n = int(input())
#     # arr = map(int, input().split())
#     # a = set(arr)
#     # a.remove(max(a))
#     # print(a)
#     a = []
#     arr = [['Harry', 37.21], ['Berry', 37.21],
#            ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#     for i in range(len(arr)):
#         a.append(arr[i][1])
#     a.remove(min(a))
#     a = min(a)
#     for i in range(len(arr)):
#         if arr[i][1] == a:
#             print(arr[i][0])
#     # print(a)
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         print(name, score)


from posixpath import split
from this import d


if __name__ == '__main__':
    n = int(input())
    a = []
    arr = []
    for _ in range(n):
        name = input()
        score = float(input())
        arr.append([name, score])
    for i in range(len(arr)):
        a.append(arr[i][1])
    a.remove(min(a))
    a = min(a)
    for i in range(len(arr)):
        if arr[i][1] == a:
            a = list(map(str, arr[i][0].split()))
            a = sorted(a)
            print(a[i])
