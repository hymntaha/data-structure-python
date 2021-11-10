def find_subsets(nums):
    subsets= []

    subsets.append([])
    for currentNumber in nums:
        n = len(subsets)
        for i in range(n):
            set1 = list(subsets[i])
            set1.append(currentNumber)
            subsets.append(set1)
    return subsets

def main():

    # print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()

'''
Since in each step, the number of subsets doubles as we add each element to all
the existing subsets, therefore, we will have a total of O(2^n) subsets, where N is the total
number of elements in the input set. 

And since we construct a new subset from an existing set, therefore, the time complexity of above algorithm
will be O(N*2^n)

Space Complexity: All the additional space used by the algo is for the output list. Since we will have a 
total of O(2^N) subsets, and each subset can take up to O(N) space, therefore, the space complexity 
of our algorithm will be O(N*2^N)
'''
