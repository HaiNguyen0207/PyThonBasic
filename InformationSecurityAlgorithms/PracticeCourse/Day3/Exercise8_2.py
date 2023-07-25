"""
Bài 8.Lesson8_1 Cài đặt thuật toán tính nghịch đảo trên Fp dùng Euclide mở rộng
Yêu cầu:
-	Nhập số nguyên tố p và số nguyên dương a thuộc [0,p-1]
-	Sử dụng thuật toán tính nghịch đảo trên Fp sử dụng thuật toán Euclide
mở rộng để tính nghịch đảo của a mod p

"""
import math


def euclide_extends_fp(number_a, number_prime_p):
    u = number_a
    v = number_prime_p
    x1 = 1
    x2 = 0
    b = number_prime_p
    while u != 1:
        q = v // u
        r = v - q * u
        x = x2 - q * x1
        v = u
        u = r
        x2 = x1
        x1 = x
    return (x1 + b) % b


def is_prime(number_p: int):
    if number_p < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(number_p) + 1)):
            if int(number_p % i) == 0:
                return False
    return True


number_p = int(input('nhập số nguyên tố p = '))
if is_prime(number_p):
    number_a = int(input(f'Nhập số a [0 {number_p - 1}] = '))
    result = euclide_extends_fp(number_a, number_p)
    print(f'{number_a}^(-1) mod{number_p} = {result}')
else:
    print("Vui lòng nhập số nguyên tố  ")
