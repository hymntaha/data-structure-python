from collections import deque

def find_permutations(nums):
    numsLength = len(nums)
    result = []
    permutations = deque()
    permutations.append([])
    for currentNumber in nums:
        # we will take all existing permutations and add the current number to create new permutations
        n = len(permutations)
        for _ in range(n):
            oldPermutation = permutations.popleft()
            # create a new permutation by adding the current number at every position
            for j in range(len(oldPermutation) + 1):
                newPermutation = list(oldPermutation)
                newPermutation.insert(j, currentNumber)
                if len(newPermutation) == numsLength:
                    result.append(newPermutation)
                else:
                    permutations.append(newPermutation)
    return result



def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()

"""
TIME COMPLEXITY: We know that there are a total of N! permutations of a set with 'N' numbers. In the algorithm above,
we are iterating through all of these permutations with the help of the two "for" loops. In each iterations, we go 
through all the current permutations to insert a new number in them. (Line 17). To insert a number into a permutation of 
size 'N' will take O(N), which makes the overall time complexity of out algorithm O(N * N!)

SPACE COMPLEXITY: All the additional space used by our algorithm is for the result list and the queue to store the intermediate
permutations. If you see closely, at any time, we don't have more than N! permutations between the result list and the queue.
Therefore the overall space complexity to store N! permutations each containing N elements will be O(N*N!)
"""


##### RECURSIVE SOLUTION:
def generate_permutations(nums):
    result = []
    generate_permutations_recursive(nums, 0, [], result)
    return result

def generate_permutations_recursive(nums, index, currentPermutation, result):
    if index == len(nums):
        result.append(currentPermutation)
    else:
        # create a new permutation by adding the current number at every position
        for i in range(len(currentPermutation)+1):
            newPermutation = list(currentPermutation)
            newPermutation.insert(i, nums[index])
            generate_permutations_recursive(nums, index+1, newPermutation,result)

def main():
    print("Here are all the permutations: " + str(generate_permutations([1, 3, 5])))


main()
