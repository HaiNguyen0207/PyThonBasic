"""
Bài 11. Viết chương trình tìm một thừa số không tầm thường
 của một số n nhập từ bàn phím
"""


def gcd(number_a, number_b):
    if (number_b == 0):
        return number_a
    return gcd(number_b, number_a % number_b)


def pollard(number_n):
    a = 2
    b = 2
    while True:
        a = int((a * a + 1) % number_n)
        b = int((b * b + 1) % number_n)
        b = int((b * b + 1) % number_n)
        d = gcd(a - b, number_n)
        if 1 < d and d < number_n:
            return d
        if d == number_n:
            return None


number_n = int(input("Nhập số n : "))
exp = pollard(number_n)
if exp == None:
    print("None")
else:
    print(exp)
    print(f"{number_n} = {exp} x {number_n // exp}")
