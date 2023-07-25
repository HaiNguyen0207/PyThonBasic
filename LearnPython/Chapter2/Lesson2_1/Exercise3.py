a = int(input("Nhập số a : "))
b = int(input("Nhập số b : "))
if a == b:
    print("EQUAL")
elif a > b:
    print(f"DIFFERENT : {a - b}")
else:
    print(f"DIFFERENT : {b - a}")
