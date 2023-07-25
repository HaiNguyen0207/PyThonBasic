# Bài 3. Tính tổng S = Lesson8_1 + 2 + 3 + ... + n.
n = int(input())
sum = 0;
for x in range(1, n + 1, 1):
    sum += x
print(sum)
