def tinhTong(number):
    s = 0

    # for i in range(0, len(number)):
    #     s += number[i]

    for e in number:
        s += e
    return s


number = [int(x) for x in input().split(" ")]
tong = tinhTong(number)
print(tong / len(number))
