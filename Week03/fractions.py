class Fractions:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(self, first_den, second_den):
   
        if first_den > second_den:
            greater = first_den
        else:
            greater = second_den

        while(True):
            if((greater % first_den == 0) and (greater % second_den == 0)):
                lcm = greater
                break
            greater += self.gcd(first_den, second_den)

        return lcm



    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return self.hash(self.numerator)

    def __eq__(self, other):
        return self.numerator/self.denominator == other.numerator/other.denominator

    def __add__(self, other):
        lcm = self.lcm(self.denominator, other.denominator)
        return "{}/{}".format(int((lcm / self.denominator * self.numerator) + (lcm / other.denominator * other.numerator)), lcm)

    def __sub__(self, other):
        lcm = self.lcm(self.denominator, other.denominator)
        return "{}/{}".format(int((lcm / self.denominator * self.numerator) - (lcm / other.denominator * other.numerator)), lcm)

    def __mul__(self, other):
        return "{}/{}".format(self.numerator * other.numerator, self.denominator * other.denominator)




a = Fractions(2, 5)
b = Fractions(8, 5)

print("Are equal ?", a == b)
print("Sum =", a + b)
print("Sub =", a - b)
print("Mul =", a * b)
