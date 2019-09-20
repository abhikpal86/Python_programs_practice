def sum(a,b):
    s=a+b
    print(s)

def sub(a,b):
    s=a-b
    return s

sum(2,3)
result = sub(9,3)
print(result)

def update(x):
    print(id(x))
    x=10
    print(id(x))
    print("x: ",x)

a = 8
update(a)
print(id(a))
print("a: ",a)