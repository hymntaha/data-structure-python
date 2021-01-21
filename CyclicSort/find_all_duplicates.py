def find_all_duplicates(nums):
    duplicateNumbers = []
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i],nums[j] = nums[j], nums[i],
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i+1:
            duplicateNumbers.append(nums[i])

    return duplicateNumbers

print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


"""
Time complexity #
The time complexity of the above algorithm is O(n)O(n).

Space complexity #
Ignoring the space required for storing the duplicates, the algorithm runs in constant space O(1)O(1).
"""
