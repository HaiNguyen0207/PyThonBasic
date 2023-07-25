def timGiaTriLonThu2(number):
    number.sort(reverse=True)
    max = number[0]
    for e in number:  # 5 5 4 3 2 1
        if e < max:
            return e


def timGiaTriNhoThu2(number):
    number.sort()
    min = number[0]
    for e in number:
        if e > min:
            return e


number = [int(x) for x in input().split(" ")]

print(f'Giá trị lớn thứ 2 = {timGiaTriLonThu2(number)}')

print(f'Giá trị lớn thứ 2 = {timGiaTriNhoThu2(number)}')
