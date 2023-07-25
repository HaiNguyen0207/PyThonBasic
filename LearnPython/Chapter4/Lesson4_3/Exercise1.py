"""
Bài Lesson8_1. Cho một ma trận gồm các phần tử là số nguyên cấp [m x n] với m, n > 0. Hãy nhập vào các
phần tử của ma trận sau đó hiển thị ma trận ra màn hình.
"""
row = int(input("Nhập số hàng : "))
col = int(input("Nhập số cột : "))
matrix = []
for i in range(row):
    matrix.append([])
    for j in range(col):
        matrix[i].append(input(f"matrix[{i}][{j}] = "))
# for i in range(row):
#     matrix.append(int(x) for x in input(f"Nhập phần tử hàng {i} : ").split())
for row in matrix:
    for e in row:
        print(e, end=" ")
    print()
