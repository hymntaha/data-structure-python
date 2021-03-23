def divide_list(nums, k):
    sigma = sum(nums)
    target, r = divmod(sigma, k)
    if r != 0:
        return False
    nums.sort(reverse=True)
    n = k
    s = 0
    while s < len(nums):
        if nums[s] < target:
            break
        elif nums[s] > target:
            return False
        else:
            n -= 1
        s += 1
    bins = [target] * n
    # remain = target * n
    def search(nums, s, bins, remain):
        if remain == 0:
            return True
        for i in range(len(bins)):
            if nums[s] <= bins[i]:
                bins[i] -= nums[s]
                if 0 < bins[i] < nums[-1]:
                    bins[i] += nums[s]
                    continue
                if search(nums, s+1, bins, remain-nums[s]):
                    return True
                bins[i] += nums[s]
        return False
    return search(nums, s, bins, target * n)

print(divide_list([2,3,5,1,2,3],2))

# [3,3,2] and [2,5,1]
