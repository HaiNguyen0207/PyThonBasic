# Bài 2. Nhập vào số nguyên dương n sau đó tính tổng bình phương các chữ số của n.
n = int(input("Enter number n = "))
result = 0;

while n > 0:
    i = n % 10;
    result =  (result + i * i);
    n = n // 10;
print(f"Result = {result}")
