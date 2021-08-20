def removeEven(arr):
    left = 0
    right = 1

    while right <= len(arr) - 1:
        if arr[left] % 2 == 1:
            left += 1
            right += 1
        elif arr[left] % 2 == 0 and arr[right] % 2 == 0:
            right += 1
        elif arr[right] % 2 == 1:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right += 1

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] % 2 == 0:
            arr.pop()


    return arr

nums = [1,2,4,5,10,6,3]
"""
1,5,4,2,10,6,3
"""

print(removeEven(nums))


