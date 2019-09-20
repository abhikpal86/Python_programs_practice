import array
from array import *

vals = array('i',[1,4,8,2,3])
print(vals)
print(vals.buffer_info())
a = len(vals)
print("Size is: ",a)

for i in vals:
    print(i)
vals.reverse()
print(vals)

newArr = array(vals.typecode,(a*a for a in vals))
for e in newArr:
    print(e, end=" ")