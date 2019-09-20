def div(a,b):
    print(a/b)

def select(funct):
    def inn(i,j):
        if i<j:
            i,j = j,i
            return funct(i,j)
        return funct(i,j)
    return inn

div2 = select(div)

div2(4,2)