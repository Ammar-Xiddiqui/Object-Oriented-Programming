# TO CALCULATE SUM OF TWO VECTOR t and m
class vector :
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def summ(v1,v2):
        x = v1.x + v2.x
        y = v1.y + v2.y
        z = v1.z + v2.z
        s = vector(x, y, z)
        print(f'sum of given two vectors is {s.x}i {s.y}j {s.z}k')

t=vector(23,54,32)
m=vector(12,41,34)
t.summ(m)
