# Bài 5. Cho số nguyên n và danh sách gồm n số nguyên. Liệt kê các số chính phương trong danh
# sách theo cặp (chỉ số, giá trị).
import math


def is_square(number: int) -> bool:
    for i in range(1, int(math.sqrt(number) + 1)):
        if number == i * i:
            return True
    return False


n = int(input("Enter size array : "))
numbers = [int(x) for x in input().split()]
for i in range(0, n):
    if is_square(numbers[i]):
        print(f"({i},{numbers[i]})", end=" ")
