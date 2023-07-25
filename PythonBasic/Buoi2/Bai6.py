n = int(input('Nhập n = '))
s = 1
for i in range(1, n + 1):
    s *= i
print(f'{n}! = {s}')
