def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    isAscending = arr[low] < arr[high]

    while low <= high:
        mid = low + (high-low) // 2

        if key == arr[mid]:
            return mid

        if isAscending:
            if key > arr[mid]:
                low = mid+1
            else:
                high = mid - 1
        else:
            if key > arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1


"""
Time complexity: O(logN)
Space complexity: O(1)
"""
def main():
    # print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    # print(binary_search([10, 6, 4], 10))
    # print(binary_search([10, 6, 4], 4))


main()
