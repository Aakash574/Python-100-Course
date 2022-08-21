
num = int(input())
# if num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# elif num % 5 == 0 and num % 3 == 0:
#     print("FizzBuzz")


for i in range(1, num+1):
    # print(i)
    if i % 3 == 0:
        i = "Fizz"
    elif i % 5 == 0:
        i = "Buzz"
    elif i % 5 == 0 and i % 3 == 0:
        i = "FizzBuzz"
    print(i)
