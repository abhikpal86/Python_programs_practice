
import array
from array import *

a = int(input("Enter the length of the array: "))
b = array('i',[])
for q in range(a):
    x = int(input("Enter the values: "))
    b.append(x)

print(b)

f = int(input("Enter the value to search: "))
p = 1
for e in b:
    if e == f:
        print("The position of the value is in: ", p)
        break
    p += 1

y = b.index(f) + 1
print(y)
