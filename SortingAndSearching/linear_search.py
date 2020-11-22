def linear_search(arr, key):

    if (len(arr) <= 0):
        return -1

    for i in range(len(arr)):
        if(arr[i] == key):
            return i
    return -1


arr = [5, 4, 1, 0, 5, 95, 4, -100, 200, 0]
key = 95

print(linear_search(arr, key))

# Linear search runs O(n) in the worst case. This is because it makes at most n comparisons, where n is the length of the list
