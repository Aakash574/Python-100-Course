if __name__ == '___main___':
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
            print(arr[1][i])
