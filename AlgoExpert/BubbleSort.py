def bubbleSort(array):
    indexing_length = len(array) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if array[i] > array[i+1]:
                sorted = False
                array[i], array[i+1] = array[i+1], array[i],
    return array


print(bubbleSort([7,5,2,9,11,1,4]))
