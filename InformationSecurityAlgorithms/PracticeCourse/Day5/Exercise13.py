"""
Bài 13. Viết chương trình kiểm tra tính nguyên tố của một số n nhập
vào từ bàn phím theo thuật toán Fermat
"""

import math


def analysis_binary(number_k):  # phân tích mũ về nhị phân
    binary = []
    while number_k > 0:
        i = number_k % 2
        binary.append(i)
        number_k = number_k // 2
    binary.reverse()
    return binary


def power(number_a, number_k,
          number_n):  # tính toán
    if number_k == 0:
        return 1
    else:
        k = analysis_binary(number_k)
        k.reverse()  # xét trọng số nhỏ nhất
        A = [0 for x in range(len(k))]
        b = [0 for x in range(len(k))]
        A[0] = number_a
        if k[0] == 1:
            b[0] = number_a
        else:
            b[0] = 1
        for i in range(1, len(k)):
            A[i] = int(math.pow(A[i - 1], 2) % number_n)
            a = b[i - 1]
            if k[i] == 1:
                b[i] = A[i] * a % number_n
            else:
                b[i] = b[i - 1]
        return b[len(b) - 1]


def fermat(n, t):
    j = 1
    for i in range(2, n - 1):
        a = i
        r = power(a, n - 1, n)
        if r != 1:
            return 'Hợp Số'
        if j >= t:
            break
        j += 1
    return 'Nguyên Tố'


t = int(input("Nhập t :"))
number_n = int(input("Nhập số n = "))
print(fermat(number_n, t))
