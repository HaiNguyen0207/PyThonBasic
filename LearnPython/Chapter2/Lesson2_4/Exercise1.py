# tìm UCLN của  a và b nhập vào bàn phím
a = int(input("Enter number a = "))
b = int(input("Enter number b = "))
value = 0;
i = 1;
while i <= a and i <= b:
    if (a % i == 0 & b % i == 0):
        value = i;
    i = i + 1;
print(f"GCD{a, b} = {value}");
