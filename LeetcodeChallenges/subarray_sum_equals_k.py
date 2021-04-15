import collections


def sumSubarrayK(arr, k):
    d = collections.defaultdict(int)
    d[0] = 1 #for first subarray k-0=k
    tmp_sum = 0;res = 0
    for i in range(len(nums)):
        tmp_sum += nums[i]
        if tmp_sum - k in d:
            res += d[tmp_sum - k]
        d[tmp_sum] += 1
    return res


k=1
nums = [1]
print(sumSubarrayK(nums,k))

"""
1,2,3
-
  -
"""
