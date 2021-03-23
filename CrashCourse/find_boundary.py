def find_boundary(arr):
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) //2
        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

print("Find boundary :", find_boundary([False, False, True, True, True]))
print("Find boundary :", find_boundary([True]))
print("Find boundary :", find_boundary([False, False, False]))
print("Find boundary :", find_boundary([False, False, True, True, True]))
print("Find boundary :", find_boundary([True, True, True, True, True]))
print("Find boundary :", find_boundary([False, True]))
