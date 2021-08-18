def sortArrayByParity(nums):
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] % 2 > nums[j] % 2:
            nums[i], nums[j] = nums[j], nums[i]

        if nums[i] % 2 == 0: i += 1
        if nums[j] % 2 == 1: j -= 1

    return nums

arr = [0,1,2]
print(sortArrayByParity(arr))
