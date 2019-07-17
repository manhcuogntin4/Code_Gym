import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
        
    def __add__(self, no):
        real=self.real+no.real
        imaginary=self.imaginary+no.imaginary
        result ="%.2f+%.2fi" % (real,imaginary)
        return result
        
    def __sub__(self, no):
        real=self.real-no.real
        imaginary=self.imaginary-no.imaginary
        result = "%.2f%.2fi" % (real, imaginary)
        return result
    def __mul__(self, no):
        real=self.real*no.real-self.imaginary*no.imaginary
        imaginary=self.real*no.imaginary+self.imaginary*no.real
        result = "%.2f+%.2fi" % (real, imaginary)
        return result

    def __truediv__(self, no):
        real=self.real*no.real+self.imaginary*no.imaginary
        imaginary=self.real*no.imaginary-self.imaginary*no.real
        factor=no.imaginary*no.imaginary+no.real*no.real
        result="%.2f-%.2fi" % (real/factor, imaginary/factor)
        return result

    def mod(self):
        real=math.sqrt(self.real*self.real+self.imaginary*self.imaginary)
        imaginary=0
        result = "%.2f+%.2fi" % (real, imaginary)
        return result

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':