def fibo(n):
    if n<0:
        print("The number which you have enter is a negative number.")
    else:
        a = 0
        b = 1
        print("Fibonacci Sequence is:",a,b, end=" ")
        for i in range(2,n):
            c = a + b
            print(c, end=(" "))
            a = b
            b = c
def maxf(m):
    if n<0:
        print("The number which you have enter is a negative number.")
    else:
        a = 0
        b = 1
        c = 1
        i = 1
        while c < m:
            c = a + b
            a = b
            b = c
            i += 1
        else:
            print("The max value is: {} and position: {}".format(a,i))

n = int(input("Enter any number: "))
fibo(n)
print()
m = int(input("Enter the maximum value: "))
maxf(m)
