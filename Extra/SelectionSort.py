from re import S
from tokenize import Double
from tracemalloc import start
from unittest import skip


def selactionSort(iter, asc=True):
    temp = iter
    string = []
    integer = []
    res = []
    for i in range(len(iter)):
        if type(temp[i]) == str:
            string.append(temp[i])
    for i in range(len(iter)):
        if type(temp[i]) == int or type(temp[i]) == float:
            integer.append(temp[i])
    for startindex in range(0, len(string)-1):
        for index in range(startindex, len(string)):
            if (string[startindex] > string[index]):
                t = string[startindex]
                string[startindex] = string[index]
                string[index] = t
        print("Pass", startindex+1, '--->', string)
    for startindex in range(0, len(integer)-1):
        for index in range(startindex, len(integer)):
            if (integer[startindex] > integer[index]):
                t = integer[startindex]
                integer[startindex] = integer[index]
                integer[index] = t
        print("Pass", startindex+1, '--->', integer)
    for i in range(len(integer)):
        res.append(integer[i])

    for i in range(len(string)):
        res.append(string[i])
    return res


if __name__ == '__main__':

    print(selactionSort([3, 4, 5, 1.3, 'zebra', 'goat',
          'ant', 'elephant', 'buffalo', -67, 78]))
