def mergeTwoSortedList(lst1,lst2):
    index_arr1 = 0
    index_arr2 = 0
    index_result = 0
    result = []

    for i in range(len(lst1)+len(lst2)):
        result.append(i)
    # Traverse Both lists and insert smaller value from arr1 or arr2
    # into result list and then increment that lists index.
    # If a list is completely traversed, while other one is left then just
    # copy all the remaining elements into result list
    while (index_arr1 < len(lst1)) and (index_arr2 < len(lst2)):
        if (lst1[index_arr1] < lst2[index_arr2]):
            result[index_result] = lst1[index_arr1]
            index_result += 1
            index_arr1 += 1
        else:
            result[index_result] = lst2[index_arr2]
            index_result += 1
            index_arr2 += 1
    while (index_arr1 < len(lst1)):
        result[index_result] = lst1[index_arr1]
        index_result += 1
        index_arr1 += 1
    while (index_arr2 < len(lst2)):
        result[index_result] = lst2[index_arr2]
        index_result += 1
        index_arr2 += 1
    return result


# print(mergeTwoSortedList([4, 5, 6], [-2, -1, 0, 7]))
print(mergeTwoSortedList([1, 3, 4, 5],[2, 6, 7, 8]))
