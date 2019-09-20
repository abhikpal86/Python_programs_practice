class topten:

    def __init__(self):
        self.val = 1

    def __iter__(self): # it gives the object of iterator at a time
        return self

    def __next__(self): # return the next value or object
        if self.val <= 70:
            num = self.val
            self.val += 7
            return num
        else:
            raise StopIteration

abc = topten()

print(next(abc))
for i in abc:
    print(i)