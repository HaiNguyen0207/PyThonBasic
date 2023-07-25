# Bài 5. Tính n! với n là số nguyên dương nhập vào từ bàn phím.
n = int(input("Enter n = "))
result = 1;
if n <= 0:
    print("INVALID !")
else:
    i = 1;
    while i <= n:
        result = result * i;
        i = i + 1;
print(f'{n} ! = {result}')
