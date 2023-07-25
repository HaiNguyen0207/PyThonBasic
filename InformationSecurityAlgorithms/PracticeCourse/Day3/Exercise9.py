"""
Bài 9: Cài đặt chương trình tính nhân bình phương có lặp a^k mod n
Yêu cầu: Nhập số nguyên dương a, k, n.
 Sử dụng thuật toán nhân bình phương có lặp để tính ak mod n
VD1: n=6784; a=3453; k=2546
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


def calculator_modulo(number_a, number_k,
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
        return k, A, b


def show_result(number_a, number_k, number_n):
    result = calculator_modulo(number_a,
                               number_k, number_n)
    k = result[0]
    A = result[1]
    b = result[2]
    t = len(k)
    print(f'{"K[i]":8}', end="")
    for i in range(t):
        print(f'{k[i]:<8}', end="")
    print(f'\n{"A":8}', end="")
    for i in range(t):
        print(f'{A[i]:<8}', end="")
    print(f'\n{"b":8}', end="")
    for i in range(t):
        print(f'{b[i]:<8}', end="")
    print()
    print()
    print(f'{number_a}^{number_k} mod({number_n})'
          f' = {b[len(b) - 1]}')


number_a = int(input('Nhập số a = '))
number_k = int(input('Nhập số k = '))
number_n = int(input('Nhập số n = '))
show_result(number_a, number_k, number_n)
