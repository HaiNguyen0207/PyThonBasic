number = [int(x) for x in input().split(" ")]
number.sort()
min = number[0]
max = number[len(number) - 1]
if min != max:
    print(f'Giá trị nhỏ nhất = {number[0]}')
    print(f'Giá trị lớn nhất = {number[len(number) - 1]}')
else:
    print('Không có giá trị nhỏ nhất và lớn nhất')
