def tong(n):
    s = 0
    for i in range(0, n + 1):
        s += i
    return s


n = int(input('Nhập n = '))
s = tong(n)
print(s)
