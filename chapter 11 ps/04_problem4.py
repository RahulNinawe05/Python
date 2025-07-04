class Complex:
    def __init__(self, r, i):
        self.r = r 
        self.i = i

    def _add_(self, c2):
        return (self.r + c2.r, self.i +c2.i)
    
    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)
    
c1 = complex(1, 2)
c2 = complex(3, 4)

print(c1 + c2)
print(c1 * c2)