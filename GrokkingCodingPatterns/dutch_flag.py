def dutch_flag(nums):
    left, right = 0, len(nums) - 1
    i = 0
    while i <= right:
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i],
            i += 1
            left += 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
    return nums



print(dutch_flag([2, 2, 0, 1, 2, 0]))
'''
2 2 0 1 2 0

0 2 0 1 2 2

0 1 0 2 2 2

'''
