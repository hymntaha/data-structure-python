def increaseList(nums):
    nums[-1] += 1

    for i in reversed(range(1, len(nums))):
        if nums[i] != 10:
            break
        nums[i] = 0
        nums [i -1] += 1

    if nums[0] == 10:
        nums[0] = 1
        nums.append(0)

    return nums

nums = [9,8,9]
increaseList(nums)
print(nums)
