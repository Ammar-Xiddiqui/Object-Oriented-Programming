 # determinant matrix
from random import *
class matrix :
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def detr(self):
        d=self.a*self.d-self.b*self.c
        return d
a=matrix(randint(1,10),randint(1,10),randint(1,10),randint(1,10))
b=matrix.detr(a)
print(b)
