def search_ceiling_of_a_number(arr, key):
    start, end = 0, len(arr)-1
    if key > arr[end]:
        return -1

    while start <= end:
        mid = start + (end - start) // 2

        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else: # found the key
            return mid


    return start

print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
