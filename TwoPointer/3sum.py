def threeSum(nums):
    nums.sort()
    N, result = len(nums), []
    for i in range(N):
        if nums[i] != nums[i-1]:
            low = i+1
            high = N-1
            sum = 0-nums[i]

            while (low<high):
                if nums[low] + nums[high] == sum:
                    result.append([nums[i], nums[low], nums[high]])
                    while (low<high and nums[low] == nums[low+1]): low += 1
                    while (low<high and nums[high] == nums[high-1]): high -= 1
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] > sum:
                    high -= 1
                else:
                    low += 1

    return result

nums = [-3, 0, 1, 2, -1, 1, -2]
print(threeSum(nums))
