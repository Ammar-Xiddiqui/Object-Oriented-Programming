# SCALAR MULTIPLE OF A VECTOR
class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def smv(self):
        a = int(input('enter any number you want to multiple '))
        self.x = self.x * a
        self.y = self.y * a
        self.z = self.z * a
        print(f'{self.x}i {self.y}j {self.z}k')
v=vector(32,12,42)
v=vector.smv(v)

        

        
