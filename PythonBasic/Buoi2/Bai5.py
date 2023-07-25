def tong(n, k):
    s = 0
    for i in range(k, n + 1):
        s += 1 / (i * i)
    return s


n = int(input('Nhập n = '))
k = int(input('Nhập k = '))

print(tong(n, k))
