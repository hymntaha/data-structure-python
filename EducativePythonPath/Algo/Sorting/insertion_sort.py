def insertion_sort(lst):

    for i in range(1, len(lst)):
        key = lst[i]

        j = i -1
        while j >= 0 and key <lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key

    return lst

print(insertion_sort([3,2,1,5,4]))

# Time complexity: O(N^2)
