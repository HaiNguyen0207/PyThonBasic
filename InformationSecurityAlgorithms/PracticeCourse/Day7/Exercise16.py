'''
Bài 16. Cài đặt thuật toán tìm kiếm mẫu P trong đoạn văn bản T kết quả trả
về vị trí xuất hiện của mẫu P theo phương pháp vét cạn
(không sử dụng hàm có sẵn)
'''


def exist(sub, P):
    for i in range(len(sub)):
        if P[i] != sub[i]:
            return False
    return True


def search_string(T, P):
    n = len(P)
    for i in range(len(T) - n + 1):
        sub = T[i:i + n]
        if sub == P:
            return i + 1
    return -1


T = input('Nhập chuỗi T = ')
P = input('Nhập chuỗi P = ')
index = search_string(T, P)
if index != -1:
    print(f'P xuất hiện T bắt đầu từ : {index}')
else:
    print('P không xuất hiện trong T')
