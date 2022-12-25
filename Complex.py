import math

class Complex:
    def __init__ (self,real,imaginary):
        self.re = real
        self.im = imaginary

    def show(self):
        print(self.re , ' + ', self.im + 'i')

    def sum(self, other):
        result_re = self.re + other.re
        result_im = self.im + other.im
        x = Complex(result_re,result_im)
        return x

    def sub(self,other):
        result_re = self.re - other.re
        result_im = self.im - other.im
        x = Complex(result_re,result_im)
        return x

    def mul(self,other):
        result_1 = math.sqrt( self.re**2 + self.im**2 )
        result_2 = math.sqrt(other.re**2 + other.im**2)
        result   = result_1*result_2
        print(result)
        return result
    