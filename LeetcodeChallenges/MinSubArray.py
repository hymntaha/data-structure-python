def minSubArrayLen(target, nums):
    length = float('inf')
    l, r = 0, 0
    total = 0
    while r < len(nums):
        total += nums[r]

        while total >= target:
            if total >= target:
                length = min(length, r - l + 1)

            total -= nums[l]
            l += 1
        r += 1

    if length == float('inf'):
        length = 0
    return length


tar = 11
arr = [1,2,3,4,5]
print(minSubArrayLen(tar, arr))
