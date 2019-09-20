a = 18
print(id(a))
b = 5
def something():
    a=4
    x = globals()['a']
    print(id(x))
    print("in fun: ",a)# Local Variable
    globals()['a'] = 23#Global variable

something()
print("Out fun: ",a)#Global variable