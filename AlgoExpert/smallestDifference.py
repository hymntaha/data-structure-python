def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    minVal = float('inf')

    first_elem = 0
    second_elem = 0

    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            extract = abs(arrayOne[i] - arrayTwo(j))
            if extract < minVal:
                minVal = extract
                first_elem = arrayOne[i]
                second_elem = arrayTwo[j]
    return [first_elem, second_elem]

'''
Time complexity: O(N^2)
Space complexity: O(1)
'''
array1 = [-1, 5, 10, 20, 28, 3]
array2 = [26, 134, 135, 15, 17]
