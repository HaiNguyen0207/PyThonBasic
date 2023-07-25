"""
Bài 12. Viết chương trình kiểm tra tính nguyên tố
của một số n nhập vào từ bàn phím
"""
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


n = int(input('Nhập n = '))
if (is_prime(n)):
    print('Nguyên Tố')
else:
    print('Hợp Số')
