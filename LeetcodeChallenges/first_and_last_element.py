def searchRange(nums, target):
    first = binarySearchFirst(nums, target)
    if first == None:
        return [-1,-1]
    last = binarySearchLast(nums, target, first)
    return [first, last]

def binarySearchFirst(nums, target):
    l, r = 0, len(nums) - 1
    firstIndex = -1
    while l <= r:
        mid = (l + r) // 2

        if target <= nums[mid]:
            if target == nums[mid]:
                firstIndex = mid
            r = mid - 1
        else:
            l = mid + 1
    return firstIndex

def binarySearchLast(nums, target, first):
    l, r = 0, len(nums) - 1
    lastIndex = first
    while l <= r:
        mid = (l + r) // 2
        if target >= nums[mid]:
            if target == nums[mid]:
                lastIndex = mid
            l = mid + 1
        else:
            r = mid - 1
    return lastIndex

print(searchRange([5,7,7,8,8,8,8,8,8,10], 8))
