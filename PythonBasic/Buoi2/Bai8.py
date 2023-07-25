import math

n = int(input('Nhập n = '))
check = True
for i in range(2, int(math.sqrt(n) + 1)):
    if n % i == 0:
        check = False
if check == True:
    print(f'{n} là số nguyên tố')
else:
    print(f'{n} không là số nguyên tố')
