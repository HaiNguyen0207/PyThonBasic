import math


def checkIsPrime(number): # kiểm tra xem n có phải là số nguyên tố ngay k
    isPrime = True;
    if number < 2:
        isPrime = False;
    else:
        bound = int(math.sqrt(number));
        for i in range(2, bound + 1, 1):
            if number % i == 0:
                isPrime = False;
    return isPrime;


number = int(input("Enter number = "))
if (checkIsPrime(number)):
    print('YES');
else:
    print("NO")
