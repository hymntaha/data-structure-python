def numSubarrayProductLessThanK(nums,k):
    if k <= 1: return 0

    prod = 1
    res = 0
    l, r = 0, 0

    while r < len(nums):
        prod *= nums[r]

        while prod >= k:
            prod = prod / nums[l]
            l += 1
        # 10, 5, 2, 6
        res += r - l + 1
        r += 1
    return res

nums = [10,5,2,6]
k = 100
print(numSubarrayProductLessThanK(nums,k))
