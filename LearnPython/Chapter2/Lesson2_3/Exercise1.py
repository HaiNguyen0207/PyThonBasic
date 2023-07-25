#Nhập một số nguyên n sau đó hiển thị các số chẵn trong đoạn [0, n].
n = int(input())
for x in range(0,n+1,1) :
    if x % 2 == 0 :
        print(x)