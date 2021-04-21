def checkSubarraySum(nums, k):
    mp = {0: -1}
    prefix_sum = 0
    for i, num in enumerate(nums):
        prefix_sum += num
        if k != 0:
            prefix_sum = prefix_sum % k
        if prefix_sum in mp:
            # I know that sum between mp[prefix_sum] + 1 and i is multiple of K, so I don't have to include mp[prefix_sum]
            if i - mp[prefix_sum] > 1:
                return True
        else:
            # if prefix_sum doesn't exists, then add its index, otherwise don't update it, i would always prefer to keep the
            # oldest index, so that I can get length of atleast 2
            mp[prefix_sum] = i

    return False

nums = [23,2,6,4,7]
k = 13

print(checkSubarraySum(nums, k))
