def sort(num):
    for i in range(0, len(num), 1): #0,1,2,3,4,5,6
        for j in range(0,len(num) - i, 1):
            if j+1 == len(num) - i:
                break
            else:
                if num[j] > num[j+1]:
                    num[j],num[j+1] = num[j+1],num[j]
nums = [5, 3, 8, 6, 7, 2, 10]
sort(nums)
print(nums)