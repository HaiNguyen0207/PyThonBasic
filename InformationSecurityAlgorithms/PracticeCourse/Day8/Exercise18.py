'''Bài 18. Cài đặt thuật toán tìm kiếm mẫu P trong đoạn văn bản T
kết quả trả về vị trí xuất hiện của mẫu P theo phương pháp Knuth-Morris-Pratt
'''


def failure(P):
    F = {}
    F[0] = -1
    F[1] = 0
    for i in range(2, len(P)):
        prefix = []  # tiền đố
        suffixes = []  # hậu tố
        j = 1
        a = 1
        k = i
        while j <= i:
            prefix.append(P[0:j])
            suffixes.append(P[a:k])
            j += 1
            a += 1
        suffixes.reverse()
        suffixes.remove('')
        value = 0
        for x in range(i - 1):
            if prefix[x] == suffixes[x]:
                value = len(prefix[x])
        F[i] = value
    return F


def search_kmp(T, P):
    M = len(P)
    N = len(T)
    F = failure(P)
    i = 0
    j = 0
    while i + j < N:
        while T[i + j] == P[j]:
            j += 1
            if j == M:
                return i + 1
        i = i + j - F[j]
        if (F[j] == -1):
            j = 0
        else:
            j = F[j]
    return -1


T = input('Nhập chuỗi T = ')
P = input('Nhập chuỗi P = ')
index = search_kmp(T, P)
if index != -1:
    print(f'P xuất hiện trong T ở vị trí {index}')
else:
    print('P không xuất hiện trong T')
