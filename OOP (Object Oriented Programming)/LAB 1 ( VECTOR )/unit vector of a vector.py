# UNIT VECTOR OF A VECTOR
from random import *
class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def mag(self):
        m=int(((self.x**2)+(self.y**2)+(self.z**2))**0.5)
        print(f'{self.x}/{m} i {self.y}/{m} j {self.z}/{m} k is unit vector of {self.x}i {self.y}j {self.z}k')
a=vector(randint(1,10),randint(1,10),randint(1,10))
b=vector.mag(a)
