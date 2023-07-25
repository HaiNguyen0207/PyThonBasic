"""
Cho p=2147483647; W=8. Với t là độ dài từ của p,
hãy nhập các giá trị a, b  [0, 2^Wt) từ bàn phím
và AD thuật toán trừ chính xác bội
 để thực hiện tính giá trị c, với c = a - b mod 2^Wt.
"""
import math


def convert_number(number, t, W) -> []:
    array = []
    while t > 0:
        value = math.pow(2, (t - 1) * W)
        q = int(number // value)  # thương
        array.append(q)
        number = int(number % value)
        t = t - 1
    return array


def show(array: []):
    for i in array:
        print(i, end=" ")
    print()




def result(array_A, array_B, t, exp):

    remember = 0  # biến nhớ ban đầu là 0
    array_C = []  # mảng c chứa kết quả
    index = t - 1
    while index >= 0:
        if array_A[index] - array_B[index] - remember < 0:
            value = int((256 + array_A[index] - array_B[index] - remember) % exp)
            array_C.append(value)
            remember = 1
        else:
            value = int((array_A[index] - array_B[index] - remember) % exp)
            array_C.append(value % exp)
            remember = 0;
        index = index - 1
    array_C.reverse()
    print(f"A - B = ({remember} , [ ", end="")
    for i in array_C:
        print(f"{int(i)} ", end="")
    print("] )")


p = 2147483647
W = 8
m = math.ceil(math.log2(p))
t = math.ceil(m / W)
number_A = int(input("Nhập số a = "))
number_B = int(input("Nhập số b = "))
array_A = convert_number(number_A, t, W)  # chuyển đổi số a về dạng mảng
array_B = convert_number(number_B, t, W)  # chuyên ổi số b về dạng mảng
# show(array_A)
# show(array_B)
result(array_A, array_B, t, math.pow(2, W))
