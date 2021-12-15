def find_subsets(nums):
    nums.sort()
    subset = []
    subset.append([])
    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0

        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex + 1

        endIndex = len(subset) - 1
        for j in range(startIndex, endIndex+1):
            set1 = list(subset[j])
            set1.append(nums[i])
            subset.append(set1)

    return subset





def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()

"""
TIME COMPLEXITY: Since, in each step, the number of subsets doubles (if not duplicates) as we add each element to all
the existing subsets, therefore, we will have a total of O(2^N) subsets, where 'N' is the total number of elements in
the input set. And since we construct a new subset from an existing set, therefore, the time complexity of the above algorithm
will be O(N*2^N)

SPACE COMPLEXITY: All the additional space used by our algorithm is for the output list. Since, at most, we will have a total
of O(2^N) subsets, and each subset can take up to O(N) space, therefore, the space complexity of our algorithm will be O(N * 2^N)
"""
