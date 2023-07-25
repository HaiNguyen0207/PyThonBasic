"""
Bài 2. Cài đặt chương trình tính tổng của hai số lớn trong hai trường hợp:
-	Mỗi số đã được cho dưới dạng một mảng biểu diễn.
Ví dụ:
P=2147483647; W=8; a=38762497; b= 568424364
A= [2    79   120     Lesson8_1]
B= [33   225   119   172]
P=2147483647; W=8
KQ A+B =(0, [36    48   239   173])
"""
import math


def check_Bit_Remeber(value, exp) -> 1 or 0:
    if value > exp:
        return 1;
    else:
        return 0


def show_Result(array_C, bitRemeber):
    print(f"( {bitRemeber} , [ ")
    array_C.reverse()
    for i in array_C:
        print(f"{i}", end=" ")
    print('\n ]')


def result(array_A, array_B, exp, t):
    remember = 0  # biến nhớ ban đầu là 0
    array_C = []
    index = t - 1
    while index >= 0:
        if array_A[index] + array_B[index] + remember > exp:
            value = int((array_A[index] + array_B[index] + remember) % exp)
            array_C.append(value)
            remember = 1
        else:
            value = int((array_A[index] + array_B[index] + remember) % exp)
            array_C.append(value % exp)
            remember = 0;
        index = index - 1
    array_C.reverse()
    print(f"A + B = ({remember} , [ ", end="")
    for i in array_C:
        print(f"{i} ", end="")
    print("] )")


P = 2147483647
W = 8
m = int(math.ceil(math.log2(P)))
t = int(math.ceil(m // W))
array_A = [int(x) for x in input("Nhập dạng mảng của số A = ").split()]
array_B = [int(x) for x in input("Nhập dạng mảng của số B = ").split()]

result(array_A, array_B, math.pow(2, W), t)
