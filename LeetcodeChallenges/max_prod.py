def maxProd(nums):
    maxProd = nums[0]
    currProd = 1

    for i in nums:
        if currProd < 0:
            currProd = 1
        currProd = currProd * i
        maxProd = max(maxProd, currProd)

    return maxProd


nums = [-3, -1, -1]
print(maxProd(nums))
