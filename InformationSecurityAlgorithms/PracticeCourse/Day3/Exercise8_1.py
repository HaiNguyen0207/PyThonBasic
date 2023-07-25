"""
Bài 8. Cài đặt thuật toán Euclide mở rộng tính ước chung lớn nhất của a và b
Yêu cầu:
-	Nhập hai số nguyên dương a và b
-	Sử dụng thuật toán Euclide mở rộng để tính gcd(a,b)
-	Nếu gcd(a,b)=1 thì tính và in a^(-1) mod b và b^(-1) mod a
Lesson8_1. VD1:  a=34568734; b=487345936

"""


def euclide_extends(number_a, number_b):
    if number_b == 0:
        d = number_a
        x = 1
        y = 0
        return d, x, y
    else:
        x1 = 1
        y1 = 0
        x2 = 0
        y2 = 1
        while number_b > 0:
            q = number_a // number_b
            r = number_a - q * number_b
            x = x2 - q * x1
            y = y2 - q * y1
            number_a = number_b
            number_b = r
            x2 = x1
            x1 = x
            y2 = y1
            y1 = y
        d = number_a
        x = x2
        y = y2
        return d, x, y


number_a = int(input("Nhập số a = "))
number_b = int(input("Nhập số b = "))
result = euclide_extends(number_a, number_b)
if result[0] != 1:
    print(f'GCD({number_a} {number_b})= {result[0]}')
    print("Không tồn tai nghịch đảo 2 số ")
else:
    print(f'GCD({number_a} {number_b})= {result[0]}')

    print(f'{number_a}^(-1) mod{number_b} ='
          f' {(result[2] + number_b) % number_b}')
    print(f'{number_b}^(-1) mod{number_a} = '
          f'{(result[1] + number_a) % number_a}')
