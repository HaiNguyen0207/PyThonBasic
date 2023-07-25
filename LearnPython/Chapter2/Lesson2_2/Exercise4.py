choice = input()
match (choice):
    case "F" | "f":
        print(f"Liệt(Trượt Môn )")
    case "D" | "d":
        print(f"Yếu")
    case "c" | "C":
        print(f"Trung Bình")
    case "b" | "B":
        print(f"Khá")
    case "a" | "A":
        print(f"Giỏi")
    case _:
        print(f"INVALID")
