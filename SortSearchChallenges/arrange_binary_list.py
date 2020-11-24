def sort_binary_list(lst):
    # Shitty way
    # return sorted(lst)

    j = 0
    for i in range(len(lst)):
        if lst[i] < 1: # Swapping with jth element if the number is less than 1
            lst[i], lst[j] = lst[j], lst[i] # Swapping
            j += 1

    return lst



lst = [1, 0, 1, 0, 1, 1, 0, 0]
print(sort_binary_list(lst))

# Time complexity is O(n) since the list is iterated only once
