# MULTIPLICATION OF TWO MATRICES
from random import *
class matrix :
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def mult(self,m2):
        a=self.a*m2.a+self.b*m2.c
        b=self.a*m2.b+self.b*m2.d
        c=self.c*m2.a+self.d*m2.c
        d=self.c*m2.b+self.d*m2.d
        ml=matrix(a,b,c,d)
        print(f'Multiplication of above two matrices is the matrix \n {ml.a}   {ml.b} \n {ml.c}   {ml.d}')
a=matrix(randint(1,10),randint(1,10),randint(1,10),randint(1,10))
b=matrix(randint(1,10),randint(1,10),randint(1,10),randint(1,10))

matrix.mult(a,b)



