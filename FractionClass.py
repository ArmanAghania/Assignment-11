import math

class Fraction:
    def __init__(self, ss, mm):
        #Properties
        self.s = ss
        self.m = mm

    def sum(self,Frac_1):
        result_s = Frac_1.s*self.m + self.s*Frac_1.m
        result_m = Frac_1.m*self.m
        x = Fraction(result_s,result_m)
        return x

    def mul(self, Frac_1):
        result_s = Frac_1.s*self.s
        result_m = Frac_1.m*self.m
        x = Fraction(result_s,result_m)
        return x

    def sub(self,Frac_1):
        result_s = Frac_1.s*self.m - self.s*Frac_1.m
        result_m = Frac_1.m*self.m
        x = Fraction(result_s,result_m)
        return x
    
    def div(self,Frac_1):
        result_s = Frac_1.s * self.m
        result_m = Frac_1.m * self.s
        x = Fraction(result_s,result_m)
        return x
    
    def frac2num(self):
        result = self.s / self.m
        return result

    def simplify(self):
        g = math.gcd(self.s,self.m)
        result_s = int(self.s/g)
        result_m = int(self.m/g)
        x = Fraction(result_s,result_m)
        return x

    def show(self):
        print(self.s, '/' , self.m)

a = Fraction(2,3)
a.show()

b = Fraction(7,1)
b.show()

# z = a.mul(b)
# z.show()

# w = b.mul(a)
# w.show()

n = a.simplify()
n.show()