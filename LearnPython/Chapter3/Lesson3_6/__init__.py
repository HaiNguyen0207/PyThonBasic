numbers = [int(x) for x in input().split()]
numbers.sort()
for i in numbers:
    print(f"{numbers[i]}",end=" ")
