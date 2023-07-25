def show_Array(array):
    for i in array:
        print(f"{i}",end=" ")


n = int(input("Nhập số lượng phần tử n =  "))
numbers = []
for i in range(n):
    numbers.append(int(input()))
show_Array(numbers)
