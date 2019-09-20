import array
from array import *

arr1 = array('i',[1,2,3,4,5])
arr2 = array('i',[6,7,8,9,10])
ar = array(arr1.typecode,[])
for i in range(4):
    ar.append(arr1[i] + arr2[i])
print(ar)

for i in range(4):
    print(ar[i],end=" ")
print()
max = 0
a = int(input("Enter the length of an array: "))
arr=array('i',[])
for i in range(a):
    n = int(input("Enter the values: "))
    arr.append(n)
    if max<arr[i]:
        max = arr[i]
print(arr)
print(max)

