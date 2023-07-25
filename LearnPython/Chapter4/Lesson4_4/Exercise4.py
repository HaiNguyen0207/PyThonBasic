"""
Bài 4. Cho hai chuỗi kí tự s1 và s2, tìm các từ chỉ xuất hiện ở chuỗi s1 hoặc s2 mà không xuất
hiện trong cả hai chuỗi này.
"""
test = int(input())
for x in range(test):
    print(f"\n Test {x + 1}")
    s1 = set(x for x in input().split())
    s2 = set(x for x in input().split())
    result = s1.difference(s2)
    result = s2.difference(s1)
    print(result)
