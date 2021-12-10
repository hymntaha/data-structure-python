def selection_sort(array):
    indexing_length = range(0, len(array) - 1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(array)):
            if array[j] < array[min_value]:
                min_value = j
        if min_value!=i:
            array[min_value], array[i] = array[i], array[min_value]

    return array
'''
Best: Time => O(n) | Space => O(1)
Average: Time => O(n^2) | Space => O(1)
Worse: Time => O(n^2) | Space => O(1)
'''
print(selection_sort([4,5,10,1,6,9,8,3,2]))
