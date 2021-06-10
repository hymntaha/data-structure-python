def checkSubarraySum(nums,k):
    s=0
    d={0:-1} # Initial sum is 0
    for i in range(len(nums)):
        s=s+nums[i]
        if k!=0:
            s=s%k
        if s in d:
            if i-d[s]>=2:
                return True
        else:
            d[s]=i
    return False

nums = [23,2,6,4,7]
k = 6
print(checkSubarraySum(nums,k))
