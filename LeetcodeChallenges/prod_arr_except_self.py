def prod_except_self(nums):
    result = [1] * len(nums)
    for i in range(1, len(nums)):
        result[i] = nums[i-1] * result[i-1]

    right_prod = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= right_prod
        right_prod *= nums[i]
    return result


nums=[1,2,3,4]
print(prod_except_self(nums))

