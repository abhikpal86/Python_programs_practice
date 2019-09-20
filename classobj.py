class computer:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def new(self):
        self.age = 33
        print(self.age)

    def change(self, other):
        if self.age == other.age:
            print("They are same age")
        else:
            print("The are not same age")

c1 = computer('abhik', 2)
c2 = computer('swati', 2)
print(c1.name, c1.age)
print(c2.name, c2.age)
c1.new()
print(c1.change(c2))