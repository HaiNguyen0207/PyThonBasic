"""
Bài 4: cài đặt phép cộng trên Fp
VD1: P=2147483647; W=8; a=2147483646; b= 2147483643
VD2: p=479001599; w=8; a= 347483646 ; b= 474836419

Yêu cầu:
-	In biểu diễn ma trận của p
-	In kết quả a+b theo tt cộng chính xác bội và giá trị bit nhớ
-	In kết quả cộng trên trường Fp

"""
import math


def show_result(result, number_p, W, t):
    remeber = result[0]
    array_c = result[1]
    number_c = value_interge(array_c, W, t)
    if remeber == 1:
        outturn = subtraction(number_c, number_p, W, t)
        return value_interge(outturn[1], W, t)
    else:
        if number_c >= number_p:
            number_c = number_c - number_p
    return number_c


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
result = addtion(number_a, number_b, W, t)
number_c = show_result(result, number_p, W, t)
print(f"P = {matrix(number_p, W, t)}")
print(f"A + B = {addtion(number_a, number_b, W, t)}")
print(f"KQ = {matrix(number_c, W, t)}")
print(value_interge(matrix(number_c, W, t), W, t))
