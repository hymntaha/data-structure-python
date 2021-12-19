def searchRange(nums, target):
    left = binarySearch(nums, target, True)
    right = binarySearch(nums, target, False)
    return [left, right]

def binarySearch(nums, target, leftBias):
    l, r = 0, len(nums) - 1
    i = -1
    while l <= r:
        m = (l+r) // 2
        if target > nums[m]:
            l = m + 1
        elif target < nums[m]:
            r = m - 1
        else:
            i = m
            if leftBias:
                r = m - 1
            else:
                l = m + 1

    return i

'''
Time Complexity: O(logN)
Space Complexity: O(1)
'''

print(searchRange([5,7,8,8,8,8],8))
