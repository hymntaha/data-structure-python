def subsetXORTotal(nums):
    result = 0
    subsets = [0]

    for n in nums:
        new_subsets = subsets.copy()
        for s in subsets:
            new_subsets.append(s^n)
            result += new_subsets[-1]
        subsets = new_subsets
    return result


nums = [5,1,6]
print(subsetXORTotal(nums))
