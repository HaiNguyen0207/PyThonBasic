# Bài Lesson8_1. Tính tổng các phần tử trong danh sách gồm n phần tử.
n = int(input("Nhập kích thước mảng n = "))
numbers = [int(x) for x in input().split()]
if len(numbers) == n:
    sum = 0
    for i in numbers:
        sum += i
    print(f"Sum = {sum}")
else:
    print("INVALID")
