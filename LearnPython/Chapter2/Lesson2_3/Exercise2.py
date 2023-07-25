# Bài 2. Nhập một số n > 0 và một số k <= n sau đó hiển thị các số lẻ trong đoạn [k, n].
k = int(input("Nhập K = "))
n = int(input("Nhập N = "))
for x in range(k, n + 1, 1):
    if x % 2 != 0:
        print(x)
