from math import gcd

class RationalError(ZeroDivisionError):
    def __init__(self, message="Denominator cannot be zero"):
        super().__init__(message)

class Rational:
    def __init__(self, numerator, denominator=None):
        if denominator is None:
            parts = numerator.split('/')
            numerator, denominator = int(parts[0]), int(parts[1])
        if denominator == 0:
            raise RationalError()
        self.n = numerator
        self.d = denominator
        self.reduce()

    def reduce(self):
        common_divisor = gcd(self.n, self.d)
        self.n //= common_divisor
        self.d //= common_divisor

    def __add__(self, other):
        if isinstance(other, Rational):
            numerator = self.n * other.d + other.n * self.d
            denominator = self.d * other.d
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            numerator = self.n + other * self.d
            return Rational(numerator, self.d)
        else:
            raise TypeError("Unsupported type for addition")

    def __sub__(self, other):
        if isinstance(other, Rational):
            numerator = self.n * other.d - other.n * self.d
            denominator = self.d * other.d
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            numerator = self.n - other * self.d
            return Rational(numerator, self.d)
        else:
            raise TypeError("Unsupported type for subtraction")

    def __mul__(self, other):
        if isinstance(other, Rational):
            numerator = self.n * other.n
            denominator = self.d * other.d
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            numerator = self.n * other
            return Rational(numerator, self.d)
        else:
            raise TypeError("Unsupported type for multiplication")

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.n == 0:
                raise RationalError("Division by zero is not allowed")
            numerator = self.n * other.d
            denominator = self.d * other.n
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            if other == 0:
                raise RationalError("Division by zero is not allowed")
            denominator = self.d * other
            return Rational(self.n, denominator)
        else:
            raise TypeError("Unsupported type for division")

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise KeyError("Invalid key")

    def __setitem__(self, key, value):
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise RationalError()
            self.d = value
        else:
            raise KeyError("Invalid key")
        self.reduce()

    def __str__(self):
        return f"{self.n}/{self.d}"

def process_expressions(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            expression = line.strip()
            try:
                result = eval(expression, {"Rational": Rational})
                outfile.write(f"{result}\n")
            except Exception as e:
                outfile.write(f"Error: {e}\n")

input_file = "input01.txt"
output_file = "output.txt"

process_expressions(input_file, output_file)