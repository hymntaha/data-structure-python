import math

def search(nums, target):
    l, r =  0 , len(nums)

    while l < r:
        m = (l + r) // 2
        if target == nums[m]:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m
    return -1


lst = [-1,0,3,5,9,12]
tar = 2

print(search(lst,tar))
