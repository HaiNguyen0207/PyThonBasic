n = int(input('Nhập n = '))
s = 1
while n > 0:
    x = n % 10
    s *= x
    n //= 10
print(s)
