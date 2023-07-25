def lietKeSoLe(n, k):
    if n >= k:
        for i in range(k, n + 1):
            if i % 2 != 0:
                print(i, end=" ")
    else:
        print('Khoảng giá trị n k không hợp lệ')


k = int(input('Nhập k = '))
n = int(input(f'Nhập n >= {k} : '))

lietKeSoLe(n, k)
