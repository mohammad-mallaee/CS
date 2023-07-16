class Rational:
    def __init__(self, n, d=1):
        self.n = n
        self.d = d

    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, value):
        if value == 0:
            raise ZeroDivisionError("Exception: denominator could not be zero")
        else:
            self.__d = value

    def __add__(self, other):
        d = self.d * other.d
        n = self.n * other.d + other.n * self.d
        return Rational(n, d)

    def __str__(self):
        return f"({self.n}, {self.d})"


r1 = Rational(2, 4)
r2 = Rational(-1, 3)
print(r1 + r2)
r3 = Rational(4)
print(r3.n, r3.d)
r3.d = 0
