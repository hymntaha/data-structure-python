def binary_search(arr,key):
    start,end = 0, len(arr) - 1
    isAscending = arr[start] < arr[end]
    while start <= end:
        # calculate the middle of the current range
        mid = start + (end-start) // 2

        if key == arr[mid]:
            return mid

        if isAscending: # ascending order
            if key < arr[mid]:
                end = mid - 1 # the key can be in the first half
            else: # key > arr[mid]
                start = mid + 1
        else: # descending order
            if key > arr[mid]:
                end = mid - 1 # the key can be in the first half
            else: # key < arr[mid]
                start = mid + 1 # The key can be in the second half

    return -1


print(binary_search([4,6,10], 10))
