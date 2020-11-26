def dutch_national_flag(lst):
    # Three-way partitioning

    size = len(lst)
    i = 0
    mid = 0
    j = size -1

    while mid <= j:
        if lst[mid] == 0:
            lst[i], lst[mid] = lst[mid], lst[i]
            i += 1
            mid += 1
        elif lst[mid] == 2:
            lst[mid],lst[j]= lst[j], lst[mid],
            j -= 1
        elif lst[mid] == 1:
            mid += 1

    return lst


# Try solving this problem in-place and in linear time without using any extra space.
lst = [2, 0, 0, 1, 2, 1, 0]
print(dutch_national_flag(lst))

""" The algorithm keeps track of the index of last zero in the list (i), the position
of the last 2 present (j), and an index mid that moves ahead only when it has found a 1
or when a 0 is swapped with any 1. 

TIME COMPLEXITY
since we are arranging the elements of the list in a single iteration, the complexity is O(N)
"""
