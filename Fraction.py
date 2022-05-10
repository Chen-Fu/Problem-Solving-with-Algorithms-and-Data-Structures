from math import gcd

# Fraction class
# Implements: addition and equality
# To do: multiplication, division, subtraction and comparison operators (< , >)

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)
        
    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)        

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __gt__(self, other_fraction):
        return self.num * other_fraction.den > self.den * other_fraction.num

    def __ge__(self, other_fraction):
        return self.num * other_fraction.den >= self.den * other_fraction.num
    
    def __lt__(self, other_fraction):
        return self.num * other_fraction.den < self.den * other_fraction.num

    def __le__(self, other_fraction):
        return self.num * other_fraction.den <= self.den * other_fraction.num
