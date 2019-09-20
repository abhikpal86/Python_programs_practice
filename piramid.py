a=int(input("Enter any number: "))

for l in range(a,0,-1):
    b=2*l-1
    c=b//2
    for i in range(c):
        print(" ",end="")
    d=a-c
    for j in range(d):
        print("# ",end="")
    e=c-1
    for k in range(e):
        print(" ",end="")
    print()