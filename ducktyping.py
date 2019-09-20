#Duck typing polymorphism

class myeditor:
    def execute(self):
        print("Compiling")
        print("Running")

class neweditor:
    def execute(self):
        print("Compiling")
        print("Running")
        print("spell check")

class Laptop:
    def code(self,idd):
        idd.execute()

pi = myeditor()
n1 = neweditor()

m1 = Laptop()
m1.code(pi)
print()
m1.code(n1)