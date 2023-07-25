#Tìm tất cả các số nguyên trong đoạn [Lesson8_1, n] chia hết cho k. Biết rằng n, k đều nguyên
#dương và giá trị của n, k không quá 10^9.
k = int(input("Nhập K = "))
n = int(input("Nhập N = "))
for x in range(1,n+1,1) :
    if x % k == 0 :
        print(x)