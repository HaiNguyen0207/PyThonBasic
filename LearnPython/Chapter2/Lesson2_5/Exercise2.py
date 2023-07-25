# Bài 2. Nhập vào hai số nguyên a, b sao cho a < b. Nhập thêm số k > 0. Liệt kê tối đa k số nguyên
# tố(nếu có) trong đoạn [a, b].
import math

a = int(input("Enter a = "))
b = int(input("Enter b = "))
k = a
while k <= b:
    is_Prime = True
    if k < 2:
        is_Prime = False
    else:
        value = 2
        while value <= math.sqrt(k):
            if k % value == 0:
                is_Prime = False
                break
            value = value + 1
    if is_Prime:
        print(f"{k}", end=" ")
    k = k + 1
