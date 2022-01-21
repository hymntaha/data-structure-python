def numOfWays(arr,k):
    nums = {}
    count = 0
    for i in range(len(arr)):
        if k - arr[i] in nums:
            count += nums[k - arr[i]]
        if arr[i] in nums:
            nums[arr[i]] += 1
        else:
            nums[arr[i]] = 1

    return count


array = [1, 5, 3, 3, 3]
k = 6
print(numOfWays(array,k))
