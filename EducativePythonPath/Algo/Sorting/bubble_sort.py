def bubble_sort(lst):

    for i in range(len(lst)):
        #Last element is already in place
        for j in range(0, len(lst) - i -1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j],

    return lst

print(bubble_sort([3,2,1,5,4]))

# Time complexity: O(N^2)
