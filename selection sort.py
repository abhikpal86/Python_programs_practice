def sort(num):
    for i in range(len(num)):
        minpos =i
        for j in range(i,len(num)):
            if num[j] < num[minpos]:
                minpos = j
        num[minpos],num[i] = num[i],num[minpos]
        print(num)
nums = [5, 3, 8, 6, 7, 2, 10]
sort(nums)
print(nums)