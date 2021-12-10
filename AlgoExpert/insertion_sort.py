def insertion_sort(array):
    indexing_length = range(1,len(array))

    for i in indexing_length:
        value_to_sort = array[i]

        while array[i-1] > value_to_sort and i>0:
            array[i], array[i-1] = array[i-1], array[i],
            i = i - 1

    return array


print(insertion_sort([3,5,1,6,9,2,11,7,8]))
'''
Best: Time => O(n) | Space => O(1)
Average: Time => O(n^2) | Space => O(1)
Worse: Time => O(n^2) | Space => O(1)
'''
