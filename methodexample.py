class student:

    school = "Hindu" #class variable

    def __init__(self, m1, m2, m3): #instance method
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def set_m1(self, value):
        self.m1 = value

    @classmethod #decorator
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("What ever you want")

s1 = student(20,25,35)
s2 = student(23, 45,67)

print("Average of s1: ", s1.avg())
print(student.getSchool())
student.info()