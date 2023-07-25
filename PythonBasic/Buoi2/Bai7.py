n = int(input('Nhập n = '))
k = int(input('Nhập k = '))
for i in range(1, n + 1):
    if i % k == 0:
        print(i)
