"""Bài 8. Kiểm tra xem số nguyên n có phải số nguyên tố hay không. Số nguyên tố là số chỉ chia hết
cho Lesson8_1 và chính nó. Biết số nguyên tố nhỏ nhất là 2."""
n = int(input())
value = 1
if n == 1:
    print("NO")
else:
    for x in range(2, n, 1):
        if n % x == 0:
            value = 0

    if value == 1:
      print("Yes")
    else:
     print("No")
