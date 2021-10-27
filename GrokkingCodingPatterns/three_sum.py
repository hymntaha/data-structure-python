def threeSum(nums):
    res = set()
    nums.sort()
    for i in range(len(nums)):
        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = nums[i] + nums[l] + nums[r]
            if three_sum == 0:
                res.add((nums[i], nums[l], nums[r]))
                r -= 1
            elif three_sum > 0:
                r -= 1
            else:
                l += 1

    return [list(i) for i in res]

print(threeSum([-3, 0, 1, 2, -1, 1, -2]))
'''
Time complexity: O(N * logN + N^2) => asymptotically O(N^2)
Space complexity: O(N)
'''
