def veHinhChuNhat(m, n):
    for i in range(1, m + 1):  # m =4 ,n = 4
        # i = 4
        for j in range(1, n + 1):
            if i == 1 or i == m or j == 1 or j == n:
                print(" * ", end=" ")
            else:
                print('   ', end=" ")
        print()


m = int(input('Nhập m = '))
n = int(input('Nhập n = '))
veHinhChuNhat(m, n)
