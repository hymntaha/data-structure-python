def selection_sort(lst):
    # Traverse through all lst elements
    for i in range(len(lst)):
        # Find the minimum element in unsorted lst
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]


lst = [3, 2, 1, 5, 4]
selection_sort(lst)  # Calling selection sort function

# Printing Sorted lst
print("Sorted lst: ", lst)

"""
Time complexity of this code is in O(N^2) because finding a min num in the list requires iterating over the 
entire list for each element of the given list. Quadratic time complexity makes it impractical for large inputs.
"""
