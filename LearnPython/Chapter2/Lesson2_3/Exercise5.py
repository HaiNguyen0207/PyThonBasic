k = int(input("Nhập K = "))
n = int(input("Nhập N = "))
sum = 0
for x in range(k, n + 1, 1):
    sum += 1 / (x * x)

print(sum)
