row = int(input("Nhập số hàng : "))
col = int(input('Nhập số cột : '))
matrix = []
for i in range(row):
    matrix.append([])
    for j in range(col):
        matrix[i].append(int(input(f"Nhập matrix[{i}{j}] = ")))
for i in matrix:
    for j in i:
        print(j, end=" ")
    print()
