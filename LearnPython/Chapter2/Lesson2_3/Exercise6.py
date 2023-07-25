# tính giai thừa K!
k = int(input("Nhập K = "))
n = int(input("Nhập N = "))
value = 1
for x in range(k, n + 1, 1):
    value *= x

print(value)
