def seen_before(arr):
    first = 0
    second = 1

    while first < len(arr) - 1:
        if arr[first] == arr[second]:
            arr.remove(arr[first])
        else:
            first += 1
            second += 1

    return arr

A = [2,3,3,3,3,5,5,6,6,6,7,11,11,11,11,13,16]
print(seen_before(A))

"""
Time complexity: O(N)
Space complexity: O(1)
"""
