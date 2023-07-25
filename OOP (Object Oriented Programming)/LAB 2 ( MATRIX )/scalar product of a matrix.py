# Scalar multilple of a matrix
from random import *
class matrix :
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def scalar_product(self):
        x=randint(1,10)
        self.a=(self.a )* x
        self.b = self.b * x
        self.c = self.c * x
        self.d = self.d * x
        print(f'scalar product of a matrix is \n {self.a}   {self.b} \n {self.c}   {self.d}')
        return self


a=matrix(randint(1,10),randint(1,10),randint(1,10),randint(1,10),)
matrix.scalar_product(a)
