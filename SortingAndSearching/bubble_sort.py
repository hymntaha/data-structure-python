def bubble_sort(lst):
    for i in range(len(lst)):

        # Last elements are already in place
        for j in range(0, len(lst) - i -1 ):
            # Traverse the list from to size of lst - i - 1
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j],


lst = [3, 2, 1, 5, 4]
bubble_sort(lst)
print(lst)
