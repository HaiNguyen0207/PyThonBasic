"""
Bài 6: Cài đặt chương trình tính phép nhân
Ví dụ 1: p=2147483647; W=8; a=524647; b= 32549
Ví dụ 2: p=2147483647; W=8; a=2348762; b= 98637

"""
import math


def value_interge(array, W, t):  # tính giá trị ngược của mảng
    value = 0
    array.reverse()
    while t > 0:
        exp = int(math.pow(2, W * (t - 1)))
        temp = int(exp * array[t - 1])
        value += temp
        t = t - 1
    return int(value)


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


def binary(uv):
    bin = [0 for x in range(16)]
    i = 0
    while uv > 0:
        bin[i] = (int(uv % 2))
        uv = uv // 2
        i = i + 1

    bin.reverse()
    return bin


def calculator_binary(array_bin: []):
    value = 0
    array_bin.reverse()
    for i in range(len(array_bin)):
        value += array_bin[i] * (math.pow(2, i))
    return value


def multiplication(number_a, number_b, number_p, W, t):
    array_a = matrix(number_a, W, t)
    array_b = matrix(number_b, W, t)
    array_a.reverse()
    array_b.reverse()
    array_c = [0 for x in range(2 * t)]
    for i in range(t):
        u = 0
        for j in range(t):
            uv = array_c[i + j] + array_a[i] * array_b[j] + u
            bin = binary(uv)
            u = int(calculator_binary(bin[0:8]))
            v = int(calculator_binary(bin[8:16]))
            array_c[i + j] = v
        array_c[i + t] = u
    array_c.reverse()
    return array_c


number_p = int(input("nhập số p = "))
W = 8
m = math.ceil(math.log2(number_p))
t = int(math.ceil(m / W))
number_a = int(input("Nhập số a = "))
number_b = int(input("Nhập số b = "))
result = multiplication(number_a, number_b, number_p, W, t)
print(result)
print(value_interge(result, W, 8))
