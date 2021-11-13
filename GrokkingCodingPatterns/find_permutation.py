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
            for j in range(len(oldPermutation)+1):
                newPermutation = list(oldPermutation)
                print(newPermutation)
                newPermutation.insert(j, currentNumber)
                if len(newPermutation) == numsLength:
                    result.append(newPermutation)
                else:
                    permutations.append(newPermutation)

    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
