# Bài 3. Cho số nguyên n và danh sách gồm n số thực. Hãy tính trung bình cộng các phần tử ở vị
# trí chẵn trong danh sách. Lưu ý vị trí trong danh sách bắt đầu từ 0.
def result(numbersList):
    index = 0
    sum = 0
    for i in range(0, n, 2):
        sum += numbersList[i]
        index = index + 1
    return sum / index


n = int(input("Enter size array : "))
numbersList = [float(x) for x in input().split()]

print(f"{result(numbersList)}")
