def cyclic_sort(nums):
    for i in range(len(nums)):
        if nums[i] != i + 1:
            nums[i] = i + 1
        else:
            continue

    return nums

Input = [3, 1, 5, 4, 2]
print(cyclic_sort(Input))
