# Bài 4. Nhập vào số nguyên dương n và kiểm tra xem n có phải số nguyên tố hay không.
import math

number = int(input("Enter number = "))
value = True;
if number == 1 or number <= 0:
    value = False;
else:
    i = 2;
    while i <= math.sqrt(number):
        if number % i == 0:
            value = False;
        i = i + 1;
if value == True:
    print("YES")
else:
    print("NO");
