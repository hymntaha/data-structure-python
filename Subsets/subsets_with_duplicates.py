def find_subsets(nums):
    # sort the numbers to handle duplicates
    list.sort(nums)
    subsets = []
    subsets.append([])
    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0
        # if current and the previous elements are same, create new subsets only from the subsets
        # added in the previous step
        if i>0 and nums[i] == nums[i-1]:
            startIndex = endIndex - 1
        endIndex = len(subsets) - 1
        for j in range(startIndex, endIndex + 1):
            # create a new subset from the existing subset and add the current element to it
            set1 = list(subsets[j])
            set1.append(nums[i])
            subsets.append(set1)
    return subsets




def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))


main()

"""
TIME COMPLEXITY: Since, in each step, the number of subsets doubles (if not duplicates) as we add each element to all
the existing subsets, therefore, we will have a total of O(2^N) subsets, where 'N' is the total number of elements in
the input set. And since we construct a new subset from an existing set, therefore, the time complexity of the above algorithm
will be O(N*2^N)

SPACE COMPLEXITY: All the additional space used by our algorithm is for the output list. Since, at most, we will have a total
of O(2^N) subsets, and each subset can take up to O(N) space, therefore, the space complexity of our algorithm will be O(N * 2^N)
"""
