def search(lst,m):
    for i in range(len(lst)):
        if lst[i] == m:
            print("The item found in position: ", i + 1)
            break
    else:
        print("The item not found.")

list = [5,8,4,6,9,2,1]
n = 9
search(list,n)
