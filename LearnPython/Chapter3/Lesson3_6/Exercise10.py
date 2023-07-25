"""
Bài 10. Cho số nguyên n, k != 0 và danh sách gồm n số nguyên. Đếm số phần tử của danh sách
chia hết cho k.
"""


def count_divisible(numbers: [], x) -> int:
    value = 0
    for i in numbers:
        if i % x == 0:
            value = value + 1
    return value


n = int(input("Enter size array : "))
numbers = [int(x) for x in input().split()]
x = int(input("Enter x = "))
print(count_divisible(numbers, x))
