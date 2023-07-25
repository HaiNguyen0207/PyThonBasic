class Fraction:
    """tử số và mẫu số"""

    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

        # phép cộng

    def addition(self, numerator_a, denominator_a,
                 numerator_b, denominator_b):
        self.numerator = denominator_b * numerator_a \
                         + denominator_a * numerator_b
        self.denominator = denominator_b * denominator_a
        self.compact()

        # phép trừ

    def subtraction(self, numerator_a, denominator_a,
                    numerator_b, denominator_b):
        self.numerator = denominator_b * numerator_a \
                         - denominator_a * numerator_b
        self.denominator = denominator_b * denominator_a
        self.compact()

        # phép nhân

    def multiplication(self, numerator_a, denominator_a,
                       numerator_b, denominator_b):
        self.numerator = numerator_a * numerator_b
        self.denominator = denominator_a * denominator_b
        self.compact()
        # phép chia

    def division(self, numerator_a, denominator_a, numerator_b,
                 denominator_b):
        self.numerator = numerator_a * denominator_b
        self.denominator = denominator_a * numerator_b
        self.compact()

    # rút gọn
    def compact(self):
        gcd = self.gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / gcd)
        self.denominator = int(self.denominator / gcd)

    def gcd(self, numerator, denominator) -> int:
        if denominator == 0:
            return numerator
        return self.gcd(denominator, numerator % denominator)

    def show_fraction(self):
        print(f"{self.numerator}/{self.denominator}", end=" ")
