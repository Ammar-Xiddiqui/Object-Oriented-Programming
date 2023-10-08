import math
# vector class
class vector:
    def __init__(self,x=0,y=0,z=0):
        self.__x=x
        self.__y=y
        self.__z=z

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,d):
        self.__x=d
        return
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, d):
        self.__y = d
        return

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, d):
        self.__z = d
        return
    def __add__(self,other):
        ans=vector()
        ans.x=self.x+other.x
        ans.y = self.y + other.y
        ans.z = self.z + other.z
        return ans
    def __str__(self):
        return f"{self.x}x {self.y}y {self.z}z  "
    def __sub__(self, other):
        ans = vector()
        ans.x = self.x - other.x
        ans.y = self.y - other.y
        ans.z = self.z - other.z
        return ans
    def __mul__(self,other):
        if type(self) ==int or type(other)== int:
            v = vector()
            v.x = self.x * other
            v.y = self.y * other
            v.z = self.z * other
            return v
        else:
            return self.x * other.x + self.y * other.y + self.z * other.z
    @staticmethod
    def cross_product(self,other):
        v = vector()
        v.x = (self.y * other.z) - (self.z * other.y)
        v.y = (self.x * other.z) - (self.z * other.x)
        v.z = (self.x * other.y) - (self.y * other.x)
        return v

    def __rmul__(self, other):
        return self.__mul__(other)
    def __truediv__(self, other):
        ans=vector()
        ans.x=self.x/other
        ans.y = self.y / other
        ans.z = self.z / other
        return ans
    @staticmethod
    def stp(self,second,third):
        return self.x*(second.y*third.z-second.z*third.y)-self.y*(second.x*third.z-second.z*third.x)\
            +self.z*(second.x*third.y-second.y*third.x)
    @staticmethod
    def mag(self):
        mag=f'{((self.x)**2+(self.y)**2+(self.z)**2)**0.5 :0.3} '
        return float(mag)
    @staticmethod
    def dot_product(self,others):
        return (self.x*others.x)+(self.y*others.y)+(self.z*others.z)
    @staticmethod
    def normalize(self):
        m=vector.mag(self)
        if m ==0:
            return self
        else:
            return f'{self.x}/{m} i   {self.y}/{m} j   {self.x}/{m} k'
    @staticmethod
    def angle_find( self,other,degrees):
        dot=vector.dot_product(self,other)
        mag_self=vector.mag(self)
        mag_other=vector.mag(other)
        if mag_other ==0 or mag_self==0:
            return 0.0 if degrees else 0
        cos_theta = dot / (mag_self * mag_other)
        if degrees==True:
            return f'{math.degrees(math.acos(cos_theta))} (in angle) '
        else :
            return f'{ math.acos(dot / (mag_self * mag_other))} (in radian) '
a=vector(2,5,5)
b=vector(5,4,4)
c=vector(9,7,6)
# print(a) #>>>to print a vector properly
# print(f'a+b is equal to {a+b}') #>>>to add two vectors
# print(f'a-b is equal to {a-b}')#>>>two subtract two vectors
# print(f'a*b is equal to ',a*2) #>>>two take scalar product of vector by an integer
# print(f'a/interger is equal to {a/3}')#>>> two divide a number by an integer
# print(f'angle between two given vectors is {vector.angle_find(a,b,False)}') #>>>two find angle between two vectors
# print(vector.mag(a)) #>>>to find magnitude of vector
# print(vector.dot_product(a,b)) #>>>to find a dot product of two vector
# print(f'the cross product of  two given vectors are {vector.cross_product(a,b)}')#>>>to take cross product of two vectors
# print(f'the normalized form of given vector is {vector.normalize(a)}')#>>>to normalize a vector
