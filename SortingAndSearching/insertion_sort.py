def insertion_sort(arr):
    for i in range(1, len(arr)):
        currentvalue = arr[i]
        position = i

        while position > 0 and arr[position-1] > currentvalue:
            arr[position] = arr[position-1]
            position = position - 1

        arr[position] = currentvalue



arr = [3, 2, 1, 5, 4]
insertion_sort(arr)
print(arr)
