m = 0
def found(list, n):
    l = 0
    u = len(list)
    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['m'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    else:
        return False

x = [11,22,33,44,55,66,77]
n = int(input("Enter the number: "))

if found(x,n):
    print("Found at position: ",m+1)
else:
    print("Not found")