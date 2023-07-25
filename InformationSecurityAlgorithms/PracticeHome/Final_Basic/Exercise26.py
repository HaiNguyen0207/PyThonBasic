'''
Câu 26. Một số được gọi là số mạnh mẽ khi nó đồng thời vừa chia hết
cho số nguyên tố và chia hết cho bình phương của số nguyên tố đó.
 Tìm số mạnh mẽ nhỏ hơn số N cho trước (N < 10000)
'''
import math


def factor_prime(n):  # phân tích ra thừa số nguyên tố
    p = []
    for i in range(2, int(math.sqrt(n) + 1)):
        while n % i == 0:
            if i not in p:
                p.append(i)
            n //= i
    if n > 1:
        p.append(n)
    return p


def check(i):
    p = factor_prime(i)
    for e in p:
        if i % e != 0 or i % (e * e) != 0:
            return False
    return True


def number_strong(n):
    for i in range(1, n + 1):
        if check(i):
            print(i, end=" ")


if __name__ == '__main__':
    n = int(input('Nhập n = '))
    if n > 0 and n < 10000:
        number_strong(n)
    else:
        print('Nhập khoảng n hợp lệ')
