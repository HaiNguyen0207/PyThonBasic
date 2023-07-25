"""
Bài 10: Viết chương trình tìm tất cả các số nguyên tố <=n với n nhập vào từ bàn phím
-	Cách thông thường
-	Sàng Erosthenes
-	Sàng phân đoạn

"""
import math

 # cách tối ưu
def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def number_prime(number_n):  # cách thông thường
    result_prime = []
    for i in range(2, number_n + 1):
        if is_prime(i):
            result_prime.append(i)
    return result_prime


def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(number) + 1)):
            if number % i == 0:
                return False
        return True


def check_prime(prime, p, number_n):
    i = 2
    while i * p <= number_n:
        prime[i * p] = 0
        i = i + 1


def sift_erosthenes(number_n):  # sàng erosthenes
    prime = {x: 1 for x in range(2, number_n + 1)}
    list_key = list(prime)
    result = []
    p = 2
    while len(list_key) > 0:
        check_prime(prime, p, number_n)
        list_key.clear()
        for i in range(p + 1, number_n + 1):
            if (prime[i] == 1):
                list_key.append(i)
        if len(list_key) > 0:
            p = min(list_key)
    for i in prime:
        if prime[i] == 1:
            result.append(i)
    return result


def sift_erosthenes_parition_first(list_first, result):
    t = max(list(list_first))
    for j in range(2, t + 1):
        p = 2
        while j * p <= t:
            list_first[j * p] = 0
            p = p + 1
    for i in list_first:
        if list_first[i] == 1:
            result.append(i)


def split_array(number_n, tenda):  # chia mảng trong phân đoạn
    row = number_n // tenda
    count = 2
    list_super = []
    for i in range(1, row):
        list_sub = {x: 1 for x in range(count, i * tenda + 2)}
        list_super.append(list_sub)
        count = i * tenda + 2
    list_super.append({x: 1 for x in range(count, number_n + 1)})
    return list_super


def check_list_next(list_next, result):
    for i in result:
        p = 2
        while i * p <= number_n:
            list_next[i * p] = 0
            p = p + 1
    for i in list_next:
        if list_next[i] == 1:
            result.append(i)


def sift_partition(number_n):  # sàng phân đoạn
    tenda = int(math.sqrt(number_n))
    list_super = split_array(number_n, tenda)  # mảng chứa các mảng con phân đoạn
    result = []  # mảng chứa các số nguyên tố
    sift_erosthenes_parition_first(list_super[0], result)
    # xét các mảng sau
    for i in range(1, len(list_super)):
        check_list_next(list_super[i], result)
    return result


number_n = int(input("Nhập số n = "))
print(f'Cách b/thường  : {number_prime(number_n)}')
print(f'Sàng erosthenes: {sift_erosthenes(number_n)}')
print(f'Sàng phân đoạn : {sift_partition(number_n)}')
