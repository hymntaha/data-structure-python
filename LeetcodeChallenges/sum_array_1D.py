def runningSum(nums):
    # i = 1
    # while i<len(nums):
    #     nums[i]+=nums[i-1]
    #     i+=1
    # return nums

    # Faster solution with O(N) space complexity
    n = len(nums)
    result = list()

    currentSum = 0
    for i in range(n):
        currentSum += nums[i]
        result.append(currentSum)

    return result

nums = [3,1,2,10,1]
print(runningSum(nums))
