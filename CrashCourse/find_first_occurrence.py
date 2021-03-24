def find_first_occurrence(arr, target):
    left, right = 0, len(arr)-1
    boundary_index = -1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            boundary_index = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return boundary_index

arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 3
print(find_first_occurrence(arr,target))

# Time complexity: O(logN)
