def gcd(number_a, number_b):
    while number_a != number_b:
        if (number_a > number_b):
            number_a = number_a - number_b;
        if (number_a < number_b):
            number_b = number_b - number_a;
    return number_a;


def lcm(number_a, number_b):
    return (number_a * number_b) // gcd(number_a, number_b);


number_a = int(input("Enter number a = "))
number_b = int(input("Enter number b = "))
print(f"GCD{number_a, number_b} = {gcd(number_a, number_b)}")
print(f"LCM{number_a, number_b} = {lcm(number_a, number_b)}")
