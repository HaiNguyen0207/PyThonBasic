"""
Bài 2. Cài đặt chương trình tính tổng của hai số lớn trong hai trường hợp:
-	Mỗi số chưa được biểu diễn thành mảng
Ví dụ:
P=2147483647; W=8; a=38762497; b= 568424364
A= [2    79   120     Lesson8_1]
B= [33   225   119   172]
P=2147483647; W=8
KQ A+B =(0, [36    48   239   173])

"""
import math


def calculator_array(W: int, t: int, a: int) -> []:
    array = []
    while t > 0:
        value: int = math.pow(2, W * (t - 1))
        q = int(a // value)  # Thương
        array.append(q)
        a = int(a % value)
        t = t - 1
    return array


def result(array_A: [], array_B: [], exp: int, len: int):
    remember = 0  # biến nhớ ban đầu là 0
    array_C = []  # mảng c chứa kết quả
    index = len - 1
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
a = int(input("Nhập số a = "))
b = int(input("Nhập số b = "))
m = int(math.ceil(math.log2(P)))
t = int(math.ceil(m / W))
array_A = calculator_array(W, t, a)
array_B = calculator_array(W, t, b)
result(array_A, array_B, int(math.pow(2, W)), t)
