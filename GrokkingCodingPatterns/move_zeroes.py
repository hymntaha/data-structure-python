def moveZeroes(nums):
    n = len(nums)

    non_zero = 0

    for i in range(n):
        if nums[i] != 0:
            nums[non_zero],nums[i] = nums[i],nums[non_zero]
            non_zero +=1
    return nums

arr = [0,1,0,3,12]
print(moveZeroes(arr))
