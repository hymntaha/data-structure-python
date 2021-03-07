def find_range(arr, key):
    result = [- 1, -1]
    result[0] = binary_search(arr, key, False)
    if result[0] != -1:  # no need to search, if 'key' is not present in the input array
        result[1] = binary_search(arr, key, True)
    return result


# modified Binary Search
def binary_search(arr, key, findMaxIndex):
    keyIndex = -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:  # key == arr[mid]
            keyIndex = mid
            if findMaxIndex:
                start = mid + 1  # search ahead to find the last index of 'key'
            else:
                end = mid - 1  # search behind to find the first index of 'key'

    return keyIndex
def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()

"""
TIME COMPLEXITY: O(logN)
SPACE COMPLEXITY: O(1)
"""
