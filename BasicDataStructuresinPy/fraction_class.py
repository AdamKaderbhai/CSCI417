class Fraction:
    
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"

# create an instance of this class
f1 = Fraction(1, 2)


def is_valid(self):
    return self.den != 0

print(f1)
print(f1.num)
'''
def multiplication(self, another_fraction):
    new_num = self.num * another_fraction.num
    new_den = self.den * another_fraction.den
    self.num, self.den = new_num, new_den

f2 = Fraction(1, 2)
show = f2.multiplication(Fraction(2, 3))'''

def __add__(self, another_fraction):
    new_num = self.num * another_fraction.den + another_fraction.num * self.den
    new_den = self.den * another_fraction.den
    
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    common = gcd(new_num, new_den)
    return Fraction(new_num // common, new_den // common)

f3 = Fraction(1, 2)













