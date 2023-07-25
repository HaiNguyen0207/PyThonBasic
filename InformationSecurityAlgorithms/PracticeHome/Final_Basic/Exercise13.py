"""
Câu 13. Viết chương trình tìm hai số nguyên tố nhỏ hơn hoặc bằng N
với N nhập vào từ bàn phím, sao cho tổng và hiệu của chúng đều
là số nguyên tố.
"""
import math
import random


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def square_integer(a, r, n):
    k = []
    while r > 0:
        k.append(r % 2)
        r //= 2
    temp = a
    if k[0] == 1:
        b = a
    else:
        b = 1
    for i in range(1, len(k)):
        temp = (temp * temp) % n
        if k[i] == 1:
            b = (b * temp) % n
    return b


def miller_rabin(n, t):  # dùng miller để xét nguyên tố
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    s = 0
    x = n - 1
    while x % 2 == 0:
        s += 1
        x //= 2
    r = x
    for i in range(1, t + 1):
        a = random.randint(2, n - 2)
        y = square_integer(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = y ** 2 % n
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True


if __name__ == '__main__':
    n = int(input())
    if n > 0:
        r = []
        for i in range(2, n + 1):
            for j in range(2, n + 1):
                if is_prime(i) and is_prime(j) \
                        and is_prime(i + j) \
                        and is_prime(i - j):
                    r.append((i, j))
        if len(r) > 0:
            print(r)
        else:
            print(f'Danh sách rỗng ')
    else:
        print('Vui lòng nhập n > 0')
