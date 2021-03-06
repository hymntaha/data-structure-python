def find_duplicate(nums):
    i = 0
    while i<len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return nums[i]

    return nums

print(find_duplicate([2, 1, 3, 3, 5, 4]))

"""
Time complexity #
The time complexity of the above algorithm is O(n)O(n).

Space complexity #
The algorithm runs in constant space O(1)O(1) but modifies the input array.
"""
