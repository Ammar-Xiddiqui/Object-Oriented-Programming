# EQUALITY TEST OF TWO VECTOR
from random import *
class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def equality(self,v):
        if self.x==v.x and self.y==v.y and self.z==v.z:
            return True
        else: return False
a=vector(randint(1,10),randint(1,10),randint(1,10))
b=vector(randint(1,10),randint(1,10),randint(1,10))
if vector.equality(a,b):
    print('both vectors are equal')
else:print('both vectors are not equal')
