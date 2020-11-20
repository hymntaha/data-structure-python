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

"""
The algo is O(N^2), which again, makes it a poor choice for large input sizes. However, notice that the complexity is
actually N^2 only when the input list is sorted in reverse. So the 'best case' complexity (when the list is sorted
in the correct order) is Ω(n).
"""
