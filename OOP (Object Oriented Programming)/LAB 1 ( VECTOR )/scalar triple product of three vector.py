# SCALAR TRIPLE PRODUCT OF THREE VECTOR
class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def stp(v1, v2, v3):
        sctp = v1.x * ((v2.y * v3.z) - (v2.z * v3.y)) - v1.y * ((v2.x * v3.z) - (v2.z * v3.x)) + v1.z * (
                (v2.x * v3.y) - (v2.y * v3.x))
        return sctp
a=vector(13,4,7)
b=vector(2,5,9)
c=vector(5,6,3)
print(a.stp(b,c))
