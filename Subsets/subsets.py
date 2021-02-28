def find_subsets(nums):
    subset = []

    subset.append([])
    for currentNumber in nums:
        n = len(subset)
        for i in range(n):
            set1 = list(subset[i])
            set1.append(currentNumber)
            subset.append(set1)

    return subset
def main():

    # print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 5])))


main()

"""
TIME COMPLEXITY: Since, in each step, the number of subsets doubles as we add each element to all the existing subsets,
therefore, we will have a total of O(2^N) subsets, where 'N' is the total number of elements in the input set.
And since we construct a new subset from an existing set, therefore, the time complexity of the above algo will be O(N*2^N)

SPACE COMPLEXITY: All the additional space used by our algorithm is for the output list. Since we will have a total of O(2^N)
subsets, and each subset can take up to O(N) space, therefore, the space complexity of our algo is O(N*2^N)
"""
