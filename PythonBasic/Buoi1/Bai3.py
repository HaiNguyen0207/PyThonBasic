import math

a = int(input('Nhập số a = '))
b = int(input('Nhập số b = '))
if a == b:
    print('a và b bằng nhau')
else:
    x = int(math.fabs(a - b))
    print(f'a và b cách nhau {x} đơn vị')
