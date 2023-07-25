def addition(number_a, number_b):
    return number_a + number_b;


def subtraction(number_a, number_b):
    return number_a + number_b;


def multiplication(numner_a, number_b):
    return numner_a * number_b;


def devision(number_a, number_b):
    if number_b == 0:
        return "NULL"
    else:
        return float(number_a / number_b);


number_a = int(input("Enter number a = "))
number_b = int(input("Enter number b = "))

print(addition(number_a, number_b));
print(subtraction(number_a, number_b));
print(multiplication(number_a, number_b));
print(devision(number_a, number_b));
