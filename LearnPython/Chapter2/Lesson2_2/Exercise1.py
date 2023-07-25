number_a = int(input("Nhập số a = "))
number_b = int(input("Nhập số b = "))
print("Lesson8_1. a + b ")
print("2. a - b ")
print("3. a * b ")
print("4. a / b ")
choice = int(input())
match (choice):
    case 1:
        print(f"{number_a} + {number_b} = {number_a + number_b}")
    case 2:
        print(f"{number_a} - {number_b} = {number_a - number_b}")
    case 3:
        print(f"{number_a} * {number_b} = {number_a * number_b}")
    case 4:
        print(f"{number_a} / {number_b} = {number_a / number_b}")
    case _:
        print(f"Sai chức năng ! Vui Lòng chọn lại")
