'''
. Viết chương trình kiểm tra tính nguyên tố của một số n
nhập vào từ bàn phím theo thuật toán Miller-rabin
'''


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
    for i in range(2, n - 1):
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


n = int(input())
if(miller_rabin(n,n)) :
    print("NT")
else:
    print("HS")