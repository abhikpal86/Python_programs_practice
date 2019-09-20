a = '3'
b = '4'
c = a + b
print(c)
print(str.__add__(a,b))

class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2
        k3 = student(r1,r2)
        return k3

    def __gt__(self, other):
        w1 = self.m1 + self.m2
        w2 = other.m1 + other.m2
        if w1>w2:
            return True
        else:
            return False


s1 = student(23,34)
s2 = student(45,56)
lki = s1 + s2
print(lki.m1)

if s1>s2:
    print("s1 win")
else:
    print("s2 wins")