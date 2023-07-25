import math


def checkSNT(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def lietKe(number):
    for i in range(0, len(number)):
        if checkSNT(number[i]):
            print(f'{i} : {number[i]}')


number = [int(x) for x in input().split(" ")]
lietKe(number)
