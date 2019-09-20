for j in range(5):
    for i in range(0,4):
        print("# ",end=(""))
    print()

a=int(input("Enter any number: "))
for j in range(a+1):
    for i in range(0,j):
        print("# ",end=(""))
    print()

a=int(input("Enter any number: "))
for j in range(a,0,-1):
    for i in range(0,j):
        print("# ",end=(""))
    print()

