a = int(input('nhập số a = '))
b = int(input('nhập số b = '))

if a == 0 and b != 0:
    print('Phương trình vô nghiệm ')
elif a == 0 and b == 0:
    print('Phương trình vô số nghiệm')
else:
    print(f'Phương trình có nghiệm = {-b / a}')
