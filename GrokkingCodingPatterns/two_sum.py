def two_sum(arr,tar):
    nums = {}  # to store numbers and their indices
    for i, num in enumerate(arr):
        if tar - num in nums:
            return [nums[tar - num], i]
        else:
            nums[arr[i]] = i

    return [-1, -1]
    # l,r = 0, len(arr) - 1
    # while l<r:
    #     if arr[l] + arr[r] == tar:
    #         return [l,r]
    #     elif arr[l] + arr[r] > tar:
    #         r -= 1
    #     else:
    #         l += 1
    # return [-1,-1]

array = [1, 2, 3, 4, 6]
target=6
print(two_sum(array,target))
