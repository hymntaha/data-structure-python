def findPeakElement(nums):
    low, high = 0, len(nums)-1
    while low < high:
        mid = (high+low) // 2
        if nums[mid] < nums[mid+1]:
            low = mid+1
        else:
            high = mid
    return low

nums = [1,2,1,3,5,6,4]
print(findPeakElement(nums))
