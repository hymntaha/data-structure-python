def search_ceiling_of_a_number(arr, key):
    n = len(arr)
    if arr[n-1] < key:
        return -1

    if arr[0] > key:
        return 0

    low, high = 0, n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if key == arr[mid]:
            return mid

        if key > arr[mid]:
            low = mid + 1
        elif key < arr[mid]:
            high = mid - 1
        else:
            return mid

    return low


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
