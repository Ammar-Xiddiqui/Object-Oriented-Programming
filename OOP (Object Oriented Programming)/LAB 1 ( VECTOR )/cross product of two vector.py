# CROSS PRODUCT OF TWO VECTOR
from random import*
class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def cross_product(self,v):
        c_p=f'{(self.y*v.z)-(self.z*v.y)}i  {(self.x*v.z)-(self.z*v.x)}j {(self.x*v.y)-(self.y*v.x)}k '
        print(c_p)
a=vector(randint(1,10),randint(1,10),randint(1,10))
b=vector(randint(1,10),randint(1,10),randint(1,10))
vector.cross_product(a,b)
