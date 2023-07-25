"""
Bài Lesson8_1:
Cho p=2 147 483 647; W=8
a.	Hãy nhập số nguyên a ∈Fp từ bàn phím và biểu diễn a thành dạng mảng của các từ W-bit.
b.	Hãy nhập một mảng của 4 từ W-bit và tính giá trị của mảng đó trong Fp.

"""
import math


def calculator(W: int, t: int, a: int) -> []:
    Array = []
    while t > 0:
        value: int = math.pow(2, W * (t - 1))
        q = int(a // value)  # Thương
        Array.append(q)
        a = int(a % value)
        t = t - 1
    return Array


def reuslt(Array: []):
    print("A = [", end="")
    for i in Array:
        print(f"{i}", end=" ")
    print("]")


P: int = 2147483647
W: int = 8;
a = int(input("Nhập số a = "))
m = int(math.ceil(math.log2(P)))
t = int(math.ceil(m / W))
array = calculator(W, t, a)
reuslt(array)
