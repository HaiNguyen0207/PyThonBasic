"""
Bài 8. Cho số nguyên n và danh sách gồm n số nguyên. Hãy tìm giá trị lớn thứ hai và nhỏ thứ hai
trong danh sách. Giả sử rằng nếu tất cả các phần tử danh sách có giá trị bằng nhau thì không
tồn tại giá trị lớn nhất, lớn thứ hai và nhỏ nhất, nhỏ thứ hai.
"""


def number_Min_Second(numbers: []) -> int:
    numbers.sort();
    for i in numbers:
        if i != int(numbers[0]):
            return i


def number_Max_Second(numbers: []) -> int:
    numbers.sort(reverse=True)
    for i in numbers:
        if i != int(numbers[0]):
            return i


n = int(input("Enter size array : "))
numbers = [int(x) for x in input().split()]
smallest_Second = number_Min_Second(numbers)
largest_Second = number_Max_Second(numbers)
if smallest_Second != largest_Second:
    print(f"Min second = {smallest_Second}")
    print(f"Max second = {largest_Second}")
else:
    print("NOT AVAILABLE.")
