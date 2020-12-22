def dutch_flag_sort(arr):
    # all elements < low are 0, and all elements > high are 2
    # all elements from >= low < i are 1
    low, high = 0, len(arr) - 1
    i = 0

    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i],
            # increment 'i' and 'low'
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else: # the case for arr[i] == 2
            arr[i], arr[high] = arr[high], arr[i]
            # decrement 'high' only, after the swap the number at index 'i' could be 0, 1 or 2
            high -= 1

arr = [1, 0, 2, 1, 0]
dutch_flag_sort(arr)
print(arr)


'''
Time complexity: O(N)
Space complexity: O(1)
'''
