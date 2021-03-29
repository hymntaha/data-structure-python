def peak_of_mountain_array(arr):
    left, right = 0, len(arr) - 1
    peak = -1

    while left <= right:
        mid = (left+right) // 2
        if mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]:
            peak = mid
            right = mid - 1
        else:
            left = mid + 1

    return peak

# print("Find Peak of mountain :", peak_of_mountain_array([0, 1, 2, 3, 2, 1, 0]))
print("Find Peak of mountain :", peak_of_mountain_array([0, 10, 3, 2, 1, 2]))
# Time complexity: O(logN)
