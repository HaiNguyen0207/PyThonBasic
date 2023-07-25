"""
Bài 5. Cho hai chuỗi kí tự s1 và s2, tìm từ có
 độ dài lớn nhất xuất hiện trong cả hai chuỗi này.
 """


def find_Max(e: str, s: set) -> str:
    value = e
    max_Len = len(e)
    for i in s:
        if len(i) > max_Len:
            value = i
    return value


test = int(input())
for i in range(test +1):
    s1 = set(x for x in input().split())
    s2 = set(x for x in input().split())
    result = set()
    for e in s1.intersection(s2):
        result.add(find_Max(e, s1.intersection(s2)))
    print(f"\nTest {i + 1} : ")
    print(result)
