# Bài 11. Cho số nguyên dương n và danh sách gồm n số nguyên. Sắp xếp các phần tử trong danh
# sách theo thứ tự tăng dần
numbers = [int(x) for x in input().split()]
numbers.sort()
for i in numbers:
    print(i, end=" ")
