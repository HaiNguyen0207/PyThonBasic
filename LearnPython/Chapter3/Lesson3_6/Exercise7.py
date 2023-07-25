"""
Bài 7. Cho số nguyên n và danh sách gồm n số nguyên. Hãy tìm giá trị lớn nhất và nhỏ nhất
trong danh sách. Giả sử rằng nếu tất cả các phần tử trong danh sách có cùng Lesson8_1 giá trị thì không
tồn tại giá trị lớn nhất, nhỏ nhất.
"""


def number_Min(numbers: []) -> int:
    min = numbers[0]
    for i in numbers:
        if i < min:
            min = i
    return min


def number_Max(numbers: []) -> int:
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max


n = int(input("Enter size array : "))
numbers = [int(x) for x in input().split()]
smallest = number_Min(numbers)
largest = number_Max(numbers)
if smallest != largest:
    print(f"Min = {smallest}")
    print(f"Max = {largest}")
else:
    print("NOT AVAILABLE.")
