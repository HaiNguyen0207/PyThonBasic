'''
Bài 15. Viết chương trình sinh số nguyên tố sử dụng kiểm tra Miller-Rabin
'''
import math
import random


def square_integer(number_a, number_k, number_n):
    k = []
    while number_k > 0:
        r = number_k % 2
        k.append(r)
        number_k //= 2
    a = number_a
    if k[0] == 1:
        b = a
    else:
        b = 1
    for i in range(1, len(k)):
        a = (a * a) % number_n
        if k[i] == 1:
            b = (b * a) % number_n
    return b


def miller_rabin(n, t):
    if n != 2 and n % 2 == 0:
        return False
    r = n - 1
    s = 0
    while r % 2 == 0:
        s += 1
        r //= 2
    k = 1
    for i in range(2, n - 2):
        a = i
        y = square_integer(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = (y * y) % n
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
        if k >= t:
            break
        k += 1
    return True


def random_serach(k, t):
    while True:
        num = random.randint(2, k)
        while num % 2 == 0 and num != 2:  # chọn ngẫu nhiên số 2
            num = random.randint(2, k)
        if miller_rabin(num, t):
            return num


k_bit = int(input('Nhập số bít = '))
if k_bit == 1:
    print("None")
else:
    k = math.pow(2, k_bit) - 1
    print(random_serach(k, 500))
