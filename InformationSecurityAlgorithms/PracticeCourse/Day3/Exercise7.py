"""
Bài 7: Cài đặt chương trình  tính ước chung lớn nhất của 2 số a và b: gcd(a,b)
Yêu cầu: nhập hai số a và b luôn dương
In số a, b
In gcd(a,b)
VD1:  a=45632454; b=23454563
VD2: 	a= 28150488 b= 10507620

"""


def gcd(number_a, number_b):
    if number_b == 0:
        return number_a
    return gcd(number_b, number_a % number_b)


number_a = int(input('Nhập số a = '))
number_b = int(input('Nhập số b = '))
print(number_a)
print(number_b)
print(f"gcd({number_a} {number_b}) ="
      f"{gcd(number_a, number_b)}")
