"""
Bài 6. Cho hai tập số nguyên t1, t2, tìm giá trị nhỏ nhất xuất hiện trong cả hai tập này.
"""


def find_Number_Min(numbers) -> int:
    numbers.sort
    return numbers[0]


test = int(input())
for i in range(test + 1):
    numbers_1 = {int(x) for x in input().split()}
    numbers_2 = {int(x) for x in input().split()}
    result = numbers_1.intersection(numbers_2)
    print(f'\nTest {i + 1} :')
    if len(result) > 0:
        print(find_Number_Min(list(result)))
    else:
        print("None")
