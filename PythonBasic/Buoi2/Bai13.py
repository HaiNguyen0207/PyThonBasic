def dem(n):
    dem = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dem += 1
    print(dem)


n = int(input('Nhập n = '))
dem(n)
