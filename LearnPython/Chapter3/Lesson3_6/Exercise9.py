"""
Bài 9. Cho số nguyên n, x và danh sách các số nguyên. Hãy tìm số lần xuất hiện của x trong danh
sách.
"""


def count_occurrences(numbers: [], x) -> int:
    value = 0
    for i in numbers:
        if i == x:
            value = value + 1
    return value


n = int(input("Enter size array : "))
numbers = [int(x) for x in input().split()]
x = int(input("Enter x = "))
print(count_occurrences(numbers, x))
