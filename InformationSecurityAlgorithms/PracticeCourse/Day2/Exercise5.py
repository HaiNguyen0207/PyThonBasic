"""
Bài 5: cài đặt thuật toán trừ trên Fp
VD2:p=433494437, a= 333294897, b= 183494999
VD3: p= 433494437, a=233294897, b= 383494999

Yêu cầu:
-	In kết quả của phép trừ chính xác bội
In kết quả của phép trừ trên Fp

"""
import math


def show_result(result, number_p, W, t):
    remeber = result[0]
    array_c = result[1]
    number_c = value_interge(array_c, W, t)
    if remeber == 1:
        output = addtion(number_c, number_p, W, t)
        return value_interge(output[1], W, t)
    return number_c


def matrix(number_p, W, t):
    p = []
    while t > 0:
        value = int(math.pow(2, W * (t - 1)))
        p.append(int(number_p // value))
        number_p = int(number_p % value)
        t = t - 1
    for i in range(len(p)):
        if p[i] > 256:
            p[i] = int(p[i] % 256)
    return p


def value_interge(array, W, t):  # tính giá trị ngược của mảng
    value = 0
    array.reverse()
    while t > 0:
        exp = int(math.pow(2, W * (t - 1)))
        temp = int(exp * array[t - 1])
        value += temp
        t = t - 1
    return int(value)


def subtraction(number_a, number_b, W, t):
    array_a = matrix(number_a, W, t)
    array_b = matrix(number_b, W, t)
    remeber = 0  # biến nhớ
    array_c = [0 for x in range(t)]
    while t > 0:

        if array_a[t - 1] - array_b[t - 1] - remeber < 0:
            array_c[t - 1] = 256 + (array_a[t - 1] - array_b[t - 1] - remeber)
            remeber = 1
        else:
            array_c[t - 1] = (array_a[t - 1] - array_b[t - 1] - remeber) % 256
            remeber = 0
        t = t - 1
    return remeber, array_c


def addtion(number_a, number_b, W, t):
    array_a = matrix(number_a, W, t)
    array_b = matrix(number_b, W, t)
    remeber = 0  # biến nhớ
    array_c = [0 for x in range(t)]
    while t > 0:
        array_c[t - 1] = (array_a[t - 1] + array_b[t - 1] + remeber) % 256
        if array_a[t - 1] + array_b[t - 1] + remeber > 256:
            remeber = 1
        else:
            remeber = 0
        t = t - 1
    return remeber, array_c


number_p = int(input("Nhập số p  = "))
W = int(input("Nhập W = "))
number_a = int(input("Nhập số a = "))
number_b = int(input("Nhập số b = "))
m = math.ceil(math.log2(number_p))
t = math.ceil(m / W)
result = subtraction(number_a, number_b, W, t)
number_c = show_result(result, number_p, W, t)
print(f"A - B = {subtraction(number_a, number_b, W, t)}")
print(f"KQ = {matrix(number_c, W, t)}")
print(f"KQ = {number_c}")
