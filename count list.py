def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

lst = [23,45,36,44,88,68]
e , o = count(lst)
print("The even number: {} and odd number: {}".format(e, o))
