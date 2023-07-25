# Bài 4. Cho số nguyên n và danh sách gồm n số nguyên. Liệt kê tất cả các phần tử là số nguyên tố
# trong danh sách theo cặp(chỉ số, giá trị).
import math


def is_Prime(number: int) -> bool:
    if (number < 2):
        return False
    else:
        for i in range(2, int(math.sqrt(number) + 1), 1):
            if number % i == 0:
                return False
    return True


n = int(input("Enter size array : "))
numbers = [int(x) for x in input().split()]
for i in range(0, n ):
    if is_Prime(numbers[i]):
        print(f"({i} ,{numbers[i]})", end=" ")
