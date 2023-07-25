# tính tống Lesson8_1+Lesson8_1/2 + Lesson8_1/3 +Lesson8_1/4..+Lesson8_1/n
n = int(input())
sum = 0
for x in range(1, n + 1, 1):
    sum += 1 / x
print(sum)
