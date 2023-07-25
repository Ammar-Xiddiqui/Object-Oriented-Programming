# ADD TWO MATRICES
from random import *
class matrix :
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def add (m1, m2):
        a = m1.a + m2.a
        b = m1.b + m2.b
        c = m1.c + m2.c
        d = m1.d + m2.d
        sm = matrix(a, b, c, d)
        print(f'Sum of above two matrices is the matrix \n {sm.a}   {sm.b} \n {sm.c}   {sm.d}')

mat1=matrix(randint(1,10),randint(1,10),randint(1,10),randint(1,10))
mat2=matrix(randint(1,10),randint(1,10),randint(1,10),randint(1,10))
matrix.add(mat1,mat2)
