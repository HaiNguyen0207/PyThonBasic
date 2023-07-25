import math


def checkSoChinhPhuong(n):
    for i in range(0, int(math.sqrt(n) + 1)):
        if i * i == n:
            return True
    return False


def lietKe(number):
    for i in range(0, len(number)):
        if checkSoChinhPhuong(number[i]):
            print(f'{i} : {number[i]}')


number = [int(x) for x in input().split(" ")]
lietKe(number)
