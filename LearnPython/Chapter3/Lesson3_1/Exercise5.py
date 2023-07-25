import math


def isPrime(i):
    value = True;
    if i < 2:
        value = False;
    else:
        for x in range(2, int(math.sqrt(i)), 1):
            if i % x == 0:
                value = False;
    return value;


def listNumberPrime(number_a, number_b):
    for i in range(number_a, number_b + 1, 1):
        if (isPrime(i)):
            print(f"{i}");


number_a = int(input("Nhập số a = "))
number_b = int(input("Nhập số b = "))
listNumberPrime(number_a,number_b)