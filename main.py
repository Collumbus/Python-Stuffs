# some behaviour that I want to implement -> write some __function__
# top-level function (__init__, __add__, ...) or top-level syntax (+, -, *, ...) -> corresponding __
# x + y    ->   __add__
# init x   ->   __init__
# rept(x)  ->   __repr__
# x()      ->   __call__

class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self): # return a printable representation of this class
        return f'Polynomial(*{self.coeffs})'

    def __add__(self, other): # performs the sum of two polynomials
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self):
        pass
p1 = Polynomial(1, 2, 3) #  x² + 2x + 3
p2 = Polynomial(3, 4, 3) # 3x² + 4x + 3