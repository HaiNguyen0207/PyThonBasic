def trungBinhCong(number):
    c = 0
    s = 0
    for i in range(0, len(number), 2):
        s += number[i]
        c += 1
    return s / c


number = [int(x) for x in input().split(" ")]
print(trungBinhCong(number))
