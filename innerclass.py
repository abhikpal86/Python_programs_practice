class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        self.lap = self.Laptop()

    def show(self):
        print("The details of the student: ",self.name, self.age, self.marks)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = "i7"
            self.ram = 16

        def show(self):
            print("The details of the student laptop: ",self.brand, self.cpu, self.ram)


a =input("Enter name: ")
b =int(input("Enter age: "))
c =int(input("Enter marks: "))
print()
s1 = Student(a, b, c)
s2 = Student("Swati", 28, 87)
lapp = Student.Laptop()

s1.show()
print()
s2.show()
print()
lapp.show()