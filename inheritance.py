class A:
    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class C:
    def __init__(self):
        print("In C init")

    def feature1(self):
        print("Feature 1C is working")

    def feature2(self):
        print("Feature 2C is working")

class B(C,A):
    def __init__(self):
        super().__init__()
        print("In B init")

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

a = B()
a.feature2()