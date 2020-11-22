def binary_search(arr, left, right, key):
    while left <= right:
        mid = left + right // 2

        # Check if key is present at mid
        if arr[mid] == key:
            return mid

        # If key is greater, ignore left half
        elif arr[mid] < key:
            left = mid + 1

        # If key is smaller, ignore right half
        else:
            right = mid - 1

    return -1

arr = [1, 2, 3, 10, 20, 40, 111, 244, 14444, 800000]
key = 111

# Function call
result = binary_search(arr, 0, len(arr) - 1, key)
print(result)

# Binary search runs i O(log(n)). This is because the list is halved at every iteration
