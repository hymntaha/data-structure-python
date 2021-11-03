def cyclic_sort(nums):
    for i in range(len(nums)):
        if nums[i] != i + 1:
            nums[i] = i + 1
        else:
            continue

    return nums

Input = [3, 1, 5, 4, 2]

def cyclic_sort2(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i],
        else:
            i += 1

    return nums


print(cyclic_sort2(Input))
