def numberFirstOfN(number_N):
    while number_N //10 > 0:
        number_N = number_N // 10;
    return number_N;


def sumOfNumberN(number_N):
    sum = 0;
    while number_N > 0:
        sum += number_N % 10;
        number_N = number_N // 10;
    return sum


def multiplicationOfNumberN(number_N):
    mul = 1;
    while number_N > 0:
        mul *= number_N % 10;
        number_N = number_N // 10
    return mul;


number_N = int(input("Enter number n = "));
print(f"Number first = {numberFirstOfN(number_N)}");
print(f"Sum = {sumOfNumberN(number_N)}")
print(f"Multiplication of number = {multiplicationOfNumberN(number_N)}")
