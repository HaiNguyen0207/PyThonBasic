# Bài Lesson8_1. Nhập vào số nguyên n. Hãy kiểm tra xem n có phải số nguyên tố hay không.
import math

n = int(input("Enter n = "));
is_Prime = True
bound = 2;
if n < 2:
    is_Prime = False;
else:
    while bound <= math.sqrt(n):
        if n % bound == 0:
            is_Prime = False;
            break
        bound = bound +1;
if is_Prime:
    print("YES");
else:
    print('NO');
