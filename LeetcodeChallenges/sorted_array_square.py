def sortedSquaredArray(arr):
    first = 0
    last = len(arr) - 1
    new_arr = [0] * len(arr)

    for i in range(len(arr)):
        if abs(arr[first]) < abs(arr[last]):
            square = arr[last]
            last -= 1
        else:
            square = arr[first]
            first += 1
        new_arr[len(arr)- 1 - i] = square * square
    return new_arr

arr = [-6,-4,-2,0,3,4,5]
print(sortedSquaredArray(arr))
