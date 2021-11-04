def find_missing_numbers(nums):
    i = 0
    while i <= len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i],nums[j] = nums[j], nums[i],
        else:
            i += 1




print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
# print(find_missing_numbers([2, 4, 1, 2]))
# print(find_missing_numbers([2, 3, 2, 1]))
