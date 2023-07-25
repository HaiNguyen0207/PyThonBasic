# Bài 2. Tính trung bình cộng các phần tử trong danh sách gồm n phần tử.
def avg(numbersList: []) -> float:
    sum = 0
    for i in numbersList:
        sum += i
    return sum / len(numbersList)


n = int(input("Enter size arr : "))
numbersList = [int(x) for x in input().split()]
result = avg(numbersList)
print(f"Avg = {result}")
