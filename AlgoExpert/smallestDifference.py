def smallestDifference(arrayOne, arrayTwo):
    # arrayOne.sort()
    # arrayTwo.sort()
    # minVal = float('inf')
    #
    # first_elem = 0
    # second_elem = 0
    #
    # for i in range(len(arrayOne)):
    #     for j in range(len(arrayTwo)):
    #         extract = abs(arrayOne[i] - arrayTwo(j))
    #         if extract < minVal:
    #             minVal = extract
    #             first_elem = arrayOne[i]
    #             second_elem = arrayTwo[j]
    # return [first_elem, second_elem]
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float('inf')
    current = float('inf')
    smallestPair = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]

        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]

        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]

    return smallestPair
'''
Optimized:
Time Complexity: O(nlogn) + O(mlogm)
Space complexity: O(1)

Brute Force
Time complexity: O(N^2)
Space complexity: O(1)
'''
array1 = [-1, 5, 10, 20, 28, 3]
array2 = [26, 134, 135, 15, 17]
print(smallestDifference(array1, array2))
