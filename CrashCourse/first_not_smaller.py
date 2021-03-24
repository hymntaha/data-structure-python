def first_not_smaller(arr, target):
    left, right = 0, len(arr)-1
    boundary_index = -1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] >= target:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index

arr = [1, 3, 3, 5, 8, 8, 10]
target = 2
print(first_not_smaller(arr,target))

# Time complexity: O(logN)
