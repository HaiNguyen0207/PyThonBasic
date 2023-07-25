"""
Bài 6. Cho số nguyên n và danh sách gồm n số nguyên. Liệt kê các số thuận nghịch trong danh
sách. Giả định rằng số thuận nghịch là các số có từ 2 chữ số trở lên sao cho khi ta đọc các chữ
số của số đó từ trái sang phải hay từ phải sang trái thì đều nhận được một giá trị không đổi.
Không xét dấu của giá trị.
"""


def reverseNumber(number: int) -> bool:
    reverse = 0;
    n = number
    while n > 0:
        reverse = int(10 * reverse + n % 10)
        n = int(n / 10)
    if number == reverse:
        return True
    else:
        return False


n = int(input("Enter size array : "))
numbers = [int(x) for x in input().split()]
for i in range(0, n):
    if reverseNumber(numbers[i]):
        print(numbers[i], end=" ")
