i=int(input("Enter the number of candy you want: "))
j=1
while j<=i:
    if j>4:
        print("Out of stock")
        break
    print("Candy")
    j+=1
print("Thank you")