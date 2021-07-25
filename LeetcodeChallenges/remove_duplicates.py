def removeDuplicates(nums):
    l  = 0
    r = 1
    n = len(nums)
    while r <= n - 1:
        if nums[l] == nums[r]:
            nums.remove(nums[l])
            n = len(nums)
        else:
            if r <= n - 1:
                l += 1
                r += 1
    return nums


arr = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(arr))

def remDupSec(nums):
    nums[:] = sorted(set(nums))
    return len(nums)

print(remDupSec(arr))
