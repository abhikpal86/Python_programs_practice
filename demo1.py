print("Enter the number range.");
a=int(input("Enter the starting number: "));
b=int(input("Enter the last number: "));
i=a;
while i<=b:
    if (i%3==0 or i%5==0):
        print(end=(""))
    else:
        print(i ,end=(" "))
    i=i+1

