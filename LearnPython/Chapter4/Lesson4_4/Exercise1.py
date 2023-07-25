"""
Bài Lesson8_1. Hiển thị các từ sao cho chúng chỉ xuất hiện duy nhất Lesson8_1 lần theo đúng thứ tự xuất hiện từ
đầu chuỗi đến cuối chuỗi.
"""
s1 = [x for x in input("Nhập chuỗi : ").split()]
result = set()
for e in s1:
    if e not in result:
        result.add(e)
for e in result:
    print(e, end=' ')
