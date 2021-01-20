def find_missing_number(nums):
    i,n = 0, len(nums)

    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i],nums[j] = nums[j],nums[i],
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i

    return n

input = [4, 0, 3, 1]
print(find_missing_number(input))
