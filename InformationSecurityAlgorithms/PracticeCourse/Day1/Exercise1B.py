"""
Bài Lesson8_1:
Cho p=2 147 483 647; W=8
a.	Hãy nhập số nguyên a ∈Fp từ bàn phím và biểu diễn a thành dạng mảng của các từ W-bit.
b.	Hãy nhập một mảng của 4 từ W-bit và tính giá trị của mảng đó trong Fp.

"""
import math


def result(array: [], t: int) -> int:
    value: int = 0
    for i in array:
        value += math.pow(2, (t - 1) * W) * i
        t = t - 1
    return value


p = 2147483647
W = 8
m = math.ceil(math.log2(p))
t = math.ceil(m / W);
array = [int(x) for x in input("Nhập mảng : ").split()]
print(int(result(array, t)))
